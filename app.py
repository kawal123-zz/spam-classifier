import streamlit as st
import pickle

# Load saved model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# App title
st.title("📧 Spam Email Detector")

st.write("Enter an email message below and check whether it is Spam or Not Spam.")

# Input text box
email_text = st.text_area("Email text")

# Predict button
if st.button("Predict"):
    if email_text.strip() == "":
        st.warning("Please enter some text")
    else:
        email_vector = vectorizer.transform([email_text])
        prediction = model.predict(email_vector)

        if prediction[0] == 1:
            st.error("🚫 This email is SPAM")
        else:
            st.success("✅ This email is NOT spam")