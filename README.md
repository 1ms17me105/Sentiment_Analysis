# Sentiment Analysis API :movie_camera:

![sent](https://github.com/nihal-DS/Sentiment_Analysis/assets/120628216/6c112d66-7537-469d-a4ff-eca159564f0d)

### Simple lightweight sentiment analysis API which is finetuned to analyse movie reviews :clapper:

## Highlights of the project:
* ### Fine-Tuning transformer based model:
  - I chose BERT and RoBERTa LLM models provided through Huggingface's🤗 `transformers` package to check pretuned accuracy on a large movie review dataset.
  - Though RoBERTa provided a higher accuracy of 95% I chose to go with BERT (which provided a base pretrained accuracy of 88%) because it was 1/3rd the size of RoBERTa.
  - BERT model was further finetuned using Full Parameter Tuning and Parameter Efficient Fine-Tuning (PEFT) method which improved the accuracy from 88% to 93%.

* ### Integrating a simple FastAPI endpoint to the model:
  - Added a simple API endpoint at ```localhost:8000/sentiment_analysis/``` which return POSITIVE :+1: or NEGATIVE :-1: label and its confidence score.
 
* ### Dockerizing the application:
  - This application has been dockerized 🐳 for faster and reliable deployment.
  - Fire up the docker desktop app and use command `docker compose up --build` in terminal to deploy the application.
 
## Demo:

![api](https://github.com/nihal-DS/Sentiment_Analysis/assets/120628216/b2f00293-1cdc-4a99-a64a-7b77c4c50b2b)
