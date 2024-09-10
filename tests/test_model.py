# tests/test_model.py
from app.prediction import predict_sentiment

def test_predict_sentiment():
    review1 = "this movie is bad"
    prediction1 = predict_sentiment(review1)
    print(f"Prediction for '{review1}': {prediction1}")

if __name__ == "__main__":
    test_predict_sentiment()
    print("Test completed.")
