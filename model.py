from transformers import pipeline
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
# from transformers import RobertaTokenizerFast, RobertaForSequenceClassification

# Use RoBERTa model for better accuracy; Model size 1.4GB
# model_name = "siebert/sentiment-roberta-large-english"
# model = RobertaForSequenceClassification.from_pretrained(model_name)
# tokenizer = RobertaTokenizerFast.from_pretrained(model_name)

# DistilBERT base accuracy - 88%; Model size 400MB
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
model = DistilBertForSequenceClassification.from_pretrained(model_name)
tokenizer = DistilBertTokenizerFast.from_pretrained(model_name)

# DistilBERT finetuned accuracy - 93%; Model size 400MB
# model_name = "DistilBERT3_Finetuned"
# model = DistilBertForSequenceClassification.from_pretrained(model_name)
# tokenizer = DistilBertTokenizerFast.from_pretrained(model_name)

classifier = pipeline("sentiment-analysis", model = model_name, tokenizer = tokenizer)


def sentiment_analysis(item):
    result = classifier(item.text)
    return {"label": result[0]["label"], "confidence_score": result[0]["score"]}

