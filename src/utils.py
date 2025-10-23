import joblib

def load_model(model_path, vectorizer_path):
    """Loads the trained  and vectorizer"""
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)

    return model, vectorizer