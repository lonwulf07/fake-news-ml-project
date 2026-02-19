import joblib

model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict_news(text):

    vector = vectorizer.transform([text])

    prediction = model.predict(vector)

    return prediction[0]