# app/prediction.py
import joblib
import re
import os

# Define the base directory (the directory of the current file)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the saved model and vectorizer
model_path = os.path.join(BASE_DIR, '..', 'models', 'sentiment_model.pkl')
vectorizer_path = os.path.join(BASE_DIR, '..', 'models', 'tfidf_vectorizer.pkl')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# Preprocessing function (should match what was used during training)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'<[^>]+>', '', text)  # Remove HTML tags
    text = re.sub(r'\d+', '', text)  # Remove digits
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

def predict_sentiment(review_text):
    # Preprocess the review text
    cleaned_text = clean_text(review_text)

    # Vectorize the cleaned text
    transformed_text = vectorizer.transform([cleaned_text])

    # Predict the sentiment using the trained model
    prediction = model.predict(transformed_text)

    # Return the predicted sentiment (e.g., 0 for negative, 1 for positive)
    return prediction[0]
