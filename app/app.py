import streamlit as st
from src.inference import predict_fake_news

st.set_page_config(page_title="Fake News Detector", page_icon=":news:",layout="centered")

st.title("Fake News Detector")
st.markdown("Enter a news articl or headline below to ceck if it's **Fake** or **Real**")

user_input = st.text_area("Enter News Text", height=200)

if st.button("Predict"):
    if user_input.strip():
        result = predict_fake_news(user_input)
        st.subheader("Prediction Result:")
        st.success(result)
    else:
        st.warning("Please enter some text to analyze")