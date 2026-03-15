import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


# Load dataset
data = pd.read_csv("spam.csv")

X = data["text"]
y = data["label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Convert text to numbers
vectorizer = CountVectorizer()

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Test model
predictions = model.predict(X_test_vec)

print("Model Accuracy:", accuracy_score(y_test, predictions))


# Test custom email
email = ["You won a free vacation"]

email_vec = vectorizer.transform(email)

prediction = model.predict(email_vec)

print("Prediction:", prediction[0])
