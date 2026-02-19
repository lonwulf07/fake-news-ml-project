import streamlit as st
import joblib

# Load model
model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


# Page config
st.set_page_config(page_title="Fake News Detector", page_icon="📰")


# Title
st.title("📰 Fake News Detection System")

st.write("Enter news text below to check whether it is Fake or Real.")


# Input box
news_text = st.text_area("Enter News Text")


# Predict button
if st.button("Predict"):

    if news_text.strip() == "":

        st.warning("Please enter some text")

    else:

        vector = vectorizer.transform([news_text])

        prediction = model.predict(vector)

        if prediction[0] == 0:

            st.error("This News is FAKE")

        else:

            st.success("This News is REAL")