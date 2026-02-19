from fastapi import FastAPI
from src.predict import predict_news

app = FastAPI()

@app.get("/")
def home():

    return {"message": "Fake News Detection API"}


@app.post("/predict")

def predict(text: str):

    result = predict_news(text)

    if result == 0:

        return {"prediction": "Fake"}

    else:

        return {"prediction": "Real"}