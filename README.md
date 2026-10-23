# CareerBot — Python AI Chatbot

A responsive browser-based chatbot that maps user messages to predefined intents using TF-IDF vectors and cosine similarity. It is a small NLP project, not a generative AI model.

## Features
- Responsive chat interface with suggested prompts.
- Flask web server and JSON chat API.
- Intent matching with a configurable similarity threshold.
- Editable intent patterns and answers in `intents.json`.
- Fallback response for unknown questions and basic request validation.
- Health endpoint at `/health`.

## Tech stack
Python, Flask, scikit-learn, TF-IDF, cosine similarity, HTML, CSS, JavaScript, JSON.

## Run locally
Python 3.10+ recommended.

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open `http://127.0.0.1:5000` in your browser. Stop the server with Ctrl+C.

## Project structure
```text
AI-Chatbot/
├── app.py
├── chatbot_engine.py
├── intents.json
├── requirements.txt
├── templates/index.html
└── static/style.css
```

## How it works
1. The engine loads intent tags, example patterns, and responses from `intents.json`.
2. TF-IDF converts example patterns into vectors.
3. Each incoming message is vectorized and compared to known patterns using cosine similarity.
4. If the best similarity clears the threshold, the matching intent's response is returned; otherwise, a fallback message is shown.

## API example
```bash
curl -X POST http://127.0.0.1:5000/api/chat -H "Content-Type: application/json" -d "{"message":"How do I prepare for an interview?"}"
```

## Limitations and next steps
This is a retrieval/intent-matching chatbot. It does not understand context across multiple turns, generate novel answers, or connect to an external LLM. Add more diverse patterns, automated tests, session-aware context, and optionally a properly secured LLM API integration if desired. Do not commit API keys or personal data.

Author-
Shivam Tripathi

GitHub: Shivamtripathi78
