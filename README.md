\# Spam Email Classifier

### LIVE DEMO : https://codectechnologiesspam-email-classifier-gviumnssxnwdwahrfqmhqi.streamlit.app/

A simple Machine Learning project that classifies emails as \*\*Spam\*\* or \*\*Not Spam (Ham)\*\* using Python and Scikit-Learn.



---



\## 📌 Project Overview



Spam emails are unwanted messages that often contain advertisements, scams, or malicious links.  

This project uses \*\*Natural Language Processing (NLP)\*\* and \*\*Machine Learning\*\* to automatically detect spam emails.



The model is trained using a small dataset and the \*\*Naive Bayes classification algorithm\*\*.



---



\## 🛠 Technologies Used



\- Python

\- Pandas

\- Scikit-learn

\- NLP (CountVectorizer)

\- Machine Learning (Naive Bayes)



---



\## 📂 Project Structure

spam-email-classifier

│

├── spam.csv

├── spam\_classifier.py

├── requirements.txt

└── README.md



---



\## 📊 Dataset



The dataset contains two columns:



| Column | Description |

|------|-------------|

| text | Email message |

| label | spam or ham |



Example:



text,label

Win a free iPhone now,spam

Call me later,ham

Free vacation offer,spam





---



\## ⚙️ Installation



Install required libraries:



pip install -r requirements.txt





---



\## ▶️ Run the Project



Run the Python script:

python spam\_classifier.py





Example Output:







Model Accuracy: 1.0

Prediction: spam





---



\## 🧠 Machine Learning Algorithm



The project uses:



\*\*Multinomial Naive Bayes\*\*

Steps:

1\. Load dataset

2\. Convert text into numerical vectors

3\. Train the model

4\. Test the model

5\. Predict new email messages



---



\## 🚀 Future Improvements



\- Use a larger dataset

\- Add GUI interface

\- Build a web application

\- Improve accuracy using advanced NLP



---



\## 👨‍💻 Author



Bilal



