import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Title
st.title("📧 Spam Email Classifier")

st.write("Enter a message and check if it is Spam or Not Spam")

# Load dataset
data = pd.read_csv("spam.csv")

X = data["text"]
y = data["label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Convert text to numbers
vectorizer = CountVectorizer()

X_train_vec = vectorizer.fit_transform(X_train)

# Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# User input
message = st.text_area("Enter your message")

# Predict
if st.button("Check Message"):

    msg_vec = vectorizer.transform([message])

    prediction = model.predict(msg_vec)

    if prediction[0] == "spam":
        st.error("🚨 This message is SPAM")
    else:
        st.success("✅ This message is NOT SPAM")