from src.utils import load_model
from src.preprocess import clean_text

def predict_fake_news(text, model_path='../model/fake_news_model.pkl', vectorizer_path='../model/vectorizer.pkl'):
    """predicts if the given text is fake or real"""
    
    model, vectorizer = load_model(model_path, vectorizer_path)
    cleaned_text = clean_text(text)
    vectorized = vectorizer.transform([cleaned_text])
    prediction = model.predict(vectorized)[0]
    label = "Real News" if prediction == 1 else "Fake News"
    return label

