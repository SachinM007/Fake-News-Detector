import re
import string
import nltk
from nltk.corpus import stopwords

#downloads stopwords
nltk.download('stopwords')

#get all english stopwords and set makes it easier and faster for search
STOPWORDS = set(stopwords.words('english'))

def clean_text(text: str) -> str:
    """
    cleans the input text by removing URLs, punctuation, numbers,
    and stopwrods. Returns cleaned lowercase text
    """

    if not isinstance(text, str):
        text = str(text)

    #Lowercase
    text = text.lower()

    #Remove URLS
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    #Remove HTML tags
    re.sub(r'<.*?>+', '', text)
    #Remove punctuation
    re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    #Remove numbers
    re.sub(r'\d+', '', text)
    #Remove extra whitespace
    re.sub(r'\s+', ' ', text).strip()
    #Remove stopwords
    words = [word for word in text.split() if word not in STOPWORDS]

    return ' '.join(words)