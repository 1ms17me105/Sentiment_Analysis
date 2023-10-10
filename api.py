from fastapi import FastAPI
from model import sentiment_analysis

app = FastAPI()

@app.get("/")
def trail():
    return {"Title": "Hello World!"}

@app.get("/sentiment_analysis/{text}")
def text_for_sentiment(text: str):
    return sentiment_analysis(text)