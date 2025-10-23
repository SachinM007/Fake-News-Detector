import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

def train_model(df, text_column, label_column, model_path, vectorizer_path):
    """
    Trains the model on the cleaned text data
    """

    X_train, X_test, y_train, y_test = train_test_split(df[text_column], df[label_column], test_size=0.2, random_state=42)

    vectorizer = TfidfVectorizer(max_features=5000)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    model = LogisticRegression(max_iter=300)
    model.fit(X_train_tfidf,y_train)

    y_pred = model.predict(X_test_tfidf)

    print("Accuracy: ",accuracy_score(y_test,y_pred))
    print("Classification Report: ",classification_report(y_test, y_pred))

    joblib.dump(model, '../model/fake_news_model.pkl')
    joblib.dump(vectorizer, '../model/vectorizer.pkl')
    print("Model and vectorizer saved")

    return model, vectorizer