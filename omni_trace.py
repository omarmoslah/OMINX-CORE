import phonenumbers
import requests

def trace(target: str) -> dict:
    result = {"target": target}
    if target.startswith("+"):
        try:
            p = phonenumbers.parse(target, None)
            result.update({
                "type": "phone",
                "international": phonenumbers.format_number(p, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
                "country": phonenumbers.region_code_for_number(p),
                "valid": phonenumbers.is_valid_number(p)
            })
        except Exception as e:
            result["error"] = str(e)
    elif "@" in target:
        try:
            resp = requests.get(f"https://emailrep.io/{target}", timeout=6).json()
            result.update({
                "type": "email",
                "deliverable": resp.get("deliverable"),
                "reputation": resp.get("reputation"),
                "suspicious": resp.get("suspicious")
            })
        except Exception as e:
            result["error"] = str(e)
    else:
        result.update({"type": "url", "note": "URL tracing قيد التطوير"})
    return result
