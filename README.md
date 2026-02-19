# 📰 Fake News Detection System (Production-Ready ML Project)

## 📌 Overview

This project is a **production-ready Machine Learning web application**
that detects whether a news article is **Fake or Real** using Natural
Language Processing and Machine Learning.

It includes:

-   End‑to‑end ML pipeline
-   Model training and evaluation
-   FastAPI backend
-   Streamlit frontend
-   Docker containerization
-   Deployment‑ready structure

This project demonstrates real‑world ML engineering skills including
model serving, API development, and frontend integration.

------------------------------------------------------------------------

## 🚀 Live Features

-   Predict Fake or Real news instantly
-   Interactive web interface using Streamlit
-   REST API using FastAPI
-   Dockerized for scalable deployment

------------------------------------------------------------------------

## 🧠 Machine Learning Details

**Algorithm Used:** PassiveAggressiveClassifier

**Vectorization:** TF‑IDF

**Dataset:** Fake and Real News Dataset

**Accuracy:** \~95--99%

------------------------------------------------------------------------

## 🏗️ Project Structure


    fake-news-ml-project/

    │

    ├── data/

    ├── models/

    │   ├── model.pkl

    │   └── vectorizer.pkl

    │

    ├── notebooks/
    
    │   └── training.ipynb

    │

    ├── src/

    │

    ├── api/

    │   └── main.py

    │

    ├── app.py

    ├── requirements.txt

    ├── Dockerfile

    └── README.md

------------------------------------------------------------------------

## ⚙️ Installation

### 1. Clone Repository

``` bash
git clone https://github.com/lonwulf07/fake-news-ml-project.git
cd fake-news-ml-project
```

------------------------------------------------------------------------

### 2. Create Virtual Environment

``` bash
python -m venv venv
venv\Scripts\activate
```

------------------------------------------------------------------------

### 3. Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Run Streamlit App

``` bash
streamlit run app.py
```

------------------------------------------------------------------------

## ▶️ Run FastAPI

``` bash
uvicorn api.main:app --reload
```

Open:

http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## 🐳 Run using Docker

Build:

``` bash
docker build -t fake-news-api .
```

Run:

``` bash
docker run -p 8000:8000 fake-news-api
```

------------------------------------------------------------------------

## 🧪 Example Prediction

Input:

President signs new healthcare bill into law

Output:

Real

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   Python
-   Scikit‑learn
-   Streamlit
-   FastAPI
-   Docker
-   Pandas
-   NumPy

------------------------------------------------------------------------

## 🎯 Skills Demonstrated

-   Machine Learning
-   NLP
-   Model Deployment
-   API Development
-   Docker
-   ML Engineering

------------------------------------------------------------------------

## 👤 Author

Mohit Sharma

GitHub: https://github.com/lonwulf07

LinkedIn: https://linkedin.com/in/lonwulf

------------------------------------------------------------------------