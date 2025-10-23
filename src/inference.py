from src.utils import load_model
from src.preprocess import clean_text
import re

def predict_fake_news(text, model_path='./model/fake_news_detector.pkl', vectorizer_path='./model/vectorizer.pkl'):
    """
    predicts if the given text is fake or real
    
    """
    # Check if it's mostly or entirely a URL
    if re.match(r'https?://\S+|www\.\S+', text.strip()):
        return "Invalid input: Only URL detected (no text content)."
    
    model, vectorizer = load_model(model_path, vectorizer_path)
    cleaned_text = clean_text(text)
    
    if len(cleaned_text.split()) < 20:
        return "Not enough information...please provide detailed news or article"
    
    vectorized = vectorizer.transform([cleaned_text])
    prediction = model.predict(vectorized)
    label = "Real News" if prediction == 1 else "Fake News"
    return label

