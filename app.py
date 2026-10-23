from flask import Flask, render_template, request, jsonify
from chatbot_engine import ChatbotEngine

app = Flask(__name__)
engine = ChatbotEngine()

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/api/chat")
def chat():
    payload = request.get_json(silent=True) or {}
    message = str(payload.get("message", "")).strip()
    if not message:
        return jsonify({"reply": "Please type a message so I can help.", "intent": "empty", "confidence": 0.0}), 400
    if len(message) > 1000:
        return jsonify({"reply": "Please keep your message under 1,000 characters.", "intent": "too_long", "confidence": 0.0}), 400
    result = engine.reply(message)
    return jsonify(result)

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
