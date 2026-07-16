import re
import contractions
import nltk

nltk.download("stopwords", quiet=True)

from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words("english"))
NEGATIONS = {"no", "not", "nor", "never", "none", "n't"}
STOPWORDS = STOPWORDS - NEGATIONS

URL_RE = re.compile(r'https?://\S+|www\.\S+')
HTML_RE = re.compile(r'<.*?>')
NON_ALPHA_RE = re.compile(r"[^a-zA-Z\s']")
MULTI_SPACE_RE = re.compile(r'\s+')


def clean_text(text):

    text = str(text).lower()

    text = URL_RE.sub(" ", text)

    text = HTML_RE.sub(" ", text)

    try:
        text = contractions.fix(text)
    except Exception:
        pass

    text = NON_ALPHA_RE.sub(" ", text)

    text = MULTI_SPACE_RE.sub(" ", text).strip()

    tokens = [
        w for w in text.split()
        if w not in STOPWORDS and len(w) > 1
    ]

    return " ".join(tokens)