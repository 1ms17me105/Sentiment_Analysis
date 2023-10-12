from fastapi import FastAPI
from model import sentiment_analysis
from pydantic import BaseModel

app = FastAPI()

class SentimentFormat(BaseModel):
    text: str

@app.get("/")
def trial():
    return {"Title": "Hello World!!"}

@app.post("/sentiment_analysis/")
def text_for_sentiment(item: SentimentFormat):
    return sentiment_analysis(item)
