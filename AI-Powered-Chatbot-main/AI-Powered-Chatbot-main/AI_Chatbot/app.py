from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)
app = FastAPI()

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat(msg: Message):

    text = msg.text.lower()
    if "hello" in text:
        answer = "Hi friend!"

    elif "password" in text:
        answer = "Click Forgot Password."

    elif "support" in text:
        answer = "Contact support@example.com"

    else:
        answer = "I don't know."

    return {"reply":answer}
