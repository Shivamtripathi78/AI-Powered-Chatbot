from pathlib import Path
import json
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

INTENTS_PATH = Path(__file__).resolve().parent / "intents.json"

class ChatbotEngine:
    """Intent-matching chatbot using TF-IDF and cosine similarity."""
    def __init__(self, threshold=0.22):
        with INTENTS_PATH.open(encoding="utf-8") as f:
            self.intents = json.load(f)["intents"]
        self.patterns, self.labels = [], []
        self.by_tag = {}
        for intent in self.intents:
            self.by_tag[intent["tag"]] = intent
            for pattern in intent["patterns"]:
                self.patterns.append(self._clean(pattern))
                self.labels.append(intent["tag"])
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), lowercase=True, strip_accents="unicode")
        self.pattern_matrix = self.vectorizer.fit_transform(self.patterns)
        self.threshold = threshold

    @staticmethod
    def _clean(text):
        return re.sub(r"\s+", " ", text.strip().lower())

    def reply(self, message):
        cleaned = self._clean(message)
        vector = self.vectorizer.transform([cleaned])
        scores = cosine_similarity(vector, self.pattern_matrix).ravel()
        best_index = int(scores.argmax())
        score = float(scores[best_index])
        tag = self.labels[best_index]
        if not cleaned or score < self.threshold:
            return {
                "reply": "I’m not sure I understood that. Try asking about greetings, my features, Python, web development, interview preparation, or contact/help.",
                "intent": "fallback", "confidence": round(score, 3)
            }
        intent = self.by_tag[tag]
        # Deterministic response is useful for reproducible demos.
        response = intent["responses"][0]
        return {"reply": response, "intent": tag, "confidence": round(score, 3)}
