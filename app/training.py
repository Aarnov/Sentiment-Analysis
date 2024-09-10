import re
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Example preprocessing functions
def clean_text(text):
    text = text.lower()
    text = re.sub(r'<[^>]+>', '', text)  # Remove HTML tags
    text = re.sub(r'\d+', '', text)  # Remove digits
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

def tokenize_text(text):
    return text.split()

def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word not in stop_words]

# Load dataset
try:
    print("Loading data...")
    data = pd.read_csv('../data/dataset.csv')  # Update path to your dataset
    print(f"Data loaded successfully with {len(data)} rows.")
except Exception as e:
    print(f"An error occurred while loading the data: {e}")
    raise

# Check if dataset is large enough
if len(data) < 2:
    raise ValueError("Dataset is too small for training.")

# No limit on data size; use all available rows
# data = data.head(1000)  # Comment or remove this line to use the entire dataset

# Preprocess the data
print("Cleaning text...")
data['cleaned_text'] = data['review'].apply(clean_text)
print("Tokenizing text...")
data['tokens'] = data['cleaned_text'].apply(tokenize_text)
print("Removing stopwords...")
data['filtered_tokens'] = data['tokens'].apply(remove_stopwords)
print("Preprocessing complete.")

# Check class distribution
print("Class distribution:")
print(data['sentiment'].value_counts())

if data['sentiment'].nunique() < 2:
    raise ValueError("Error: Dataset does not contain multiple classes.")

# Vectorization using TF-IDF
try:
    print("Vectorizing text...")
    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(data['cleaned_text'])
    y = data['sentiment'].map({'positive': 1, 'negative': 0})  # Convert sentiment to numerical labels
    print(f"Text vectorized with shape: {X.shape}.")
except Exception as e:
    print(f"An error occurred during vectorization: {e}")
    raise

# Train-test split
try:
    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Data split into training set with {X_train.shape[0]} samples and test set with {X_test.shape[0]} samples.")
except Exception as e:
    print(f"An error occurred during train-test split: {e}")
    raise

# Train a model
try:
    print("Training model...")
    model = LogisticRegression()
    model.fit(X_train, y_train)
    print("Model trained successfully.")
except Exception as e:
    print(f"An error occurred during model training: {e}")
    raise

# Evaluate the model
try:
    print("Evaluating model...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy}")
except Exception as e:
    print(f"An error occurred during model evaluation: {e}")
    raise

# Save the model and vectorizer
try:
    print("Saving model and vectorizer...")
    joblib.dump(model, '../models/sentiment_model.pkl')
    joblib.dump(vectorizer, '../models/tfidf_vectorizer.pkl')
    print("Model and vectorizer saved successfully.")
except Exception as e:
    print(f"An error occurred while saving the model and vectorizer: {e}")
    raise

print("Training complete.")
