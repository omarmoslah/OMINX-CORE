# 🧠 OMNIX-CORE

OMNIX-CORE هو محرك ذكي يتعرف على نوع الهدف (رقم / بريد / رابط) ويعطيك معلومات مفيدة.

## 🔍 API Endpoint

```
GET /trace?token=OMX_TOKEN&target=VALUE
```

### 🎯 Params:
- `token`: رمز الحماية (تحطه في متغير بيئة `OMX_TOKEN`)
- `target`: القيمة المراد تتبعها (رقم، بريد أو رابط)

## 🧪 الأمثلة:

- تتبع رقم: `+216...`
- تتبع بريد: `example@gmail.com`
- تتبع رابط: `http://...`

## 🚀 التشغيل المحلي:

```bash
pip install -r requirements.txt
OMX_TOKEN=12345 python server.py
```

---

## 🔒 ملاحظة
تم حماية الـ API بتوكن لمنع الاستعمال العشوائي.
