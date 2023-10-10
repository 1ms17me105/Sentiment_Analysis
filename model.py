from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification


model_name = "distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

classifier = pipeline("sentiment-analysis", model = model_name, tokenizer = tokenizer)
# results = classifier("I am happy!!")

# print(results)

def sentiment_analysis(text: str):
    result = classifier(text)
    return {"label": result[0]["label"], "confidence_score": result[0]["score"]}

# print(sentiment_analysis("I am happy!!"))