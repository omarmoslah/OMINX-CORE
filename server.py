from flask import Flask, request, jsonify
from omni_trace import trace
import os

app = Flask(__name__)
OMX_TOKEN = os.getenv("OMX_TOKEN", "")

@app.route("/trace", methods=["GET"])
def api_trace():
    token = request.args.get("token", "")
    target = request.args.get("target", "")
    if token != OMX_TOKEN or not target:
        return jsonify({"error": "Unauthorized or missing target"}), 401
    return jsonify(trace(target))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
