# 📧 Spam Email Detector

A Machine Learning-based web application that detects whether an email message is **Spam** or **Not Spam** using Natural Language Processing (NLP) techniques.

Built with **Python, Scikit-learn, and Streamlit**.

---

## 🚀 Project Overview

Spam emails are unwanted messages that may contain advertisements, phishing links, or malicious content.  
This project uses a trained Machine Learning model to automatically classify email text as:

- 🚫 Spam  
- ✅ Not Spam (Ham)

The model is trained using text vectorization techniques and deployed through a simple Streamlit web interface.

---

## 🛠️ Technologies Used

- Python
- Scikit-learn
- Streamlit
- Pickle
- NumPy
- Pandas
- Natural Language Processing (NLP)

---

## 📂 Project Structure

```
spam-email-detector/
│
├── spam_classifier.ipynb   # Model training notebook
├── model.pkl               # Trained ML model
├── vectorizer.pkl          # Saved text vectorizer
├── app.py                  # Streamlit web application
└── README.md               # Project documentation
```

---

## 🧠 How It Works

### 1️⃣ Text Vectorization
The input email text is converted into numerical features using a trained vectorizer (CountVectorizer or TF-IDF).

### 2️⃣ Model Prediction
The saved classification model predicts whether the email is Spam or Not Spam.

### 3️⃣ Result Display
The application displays:
- 🚫 "This email is SPAM"
- ✅ "This email is NOT spam"

---

## 💻 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/spam-email-detector.git
cd spam-email-detector
```

### 2️⃣ Install Required Libraries

If you have a requirements file:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit scikit-learn pandas numpy
```

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

## 🧪 Example Usage

**Input:**
```
Congratulations! You have won a free lottery. Click here to claim your prize.
```

**Output:**
```
🚫 This email is SPAM
```

---

## 📊 Model Training

The `spam_classifier.ipynb` notebook includes:

- Data preprocessing
- Text cleaning
- Feature extraction (Vectorization)
- Model training
- Model evaluation
- Saving model and vectorizer using pickle

---

## 🔮 Future Improvements

- Display prediction probability
- Show model accuracy in UI
- Add multiple model comparison
- Deploy to Streamlit Cloud
- Improve UI design

---

## 📌 Key Features

✔ Simple and clean UI  
✔ Real-time prediction  
✔ Pre-trained ML model  
✔ Fast and lightweight  
✔ Easy to deploy  

---

⭐ If you found this project useful, consider giving it a star!
