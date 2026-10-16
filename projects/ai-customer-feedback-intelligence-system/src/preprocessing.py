"""Data loading, cleaning and text preprocessing."""
from pathlib import Path

import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

DEFAULT_DATA_PATH = Path("data") / "Womens Clothing E-Commerce Reviews.csv"
KEEP_COLUMNS = ["Review Text", "Rating", "Class Name", "Recommended IND"]
RENAME_COLUMNS = {
    "Class Name": "Product Category",
    "Recommended IND": "Recommendation Indicator",
}


def ensure_nltk_data() -> None:
    """Download the NLTK resources used by clean_text (no-op if present)."""
    for resource in ("punkt", "punkt_tab", "stopwords"):
        nltk.download(resource, quiet=True)


def get_sentiment(rating: int) -> str:
    """Rating-derived label: <=2 Negative, 3 Neutral, >=4 Positive."""
    if rating <= 2:
        return "Negative"
    if rating == 3:
        return "Neutral"
    return "Positive"


def clean_text(text: str, stop_words=None) -> str:
    """Lower-case, tokenize, keep alphabetic tokens, drop English stopwords."""
    if stop_words is None:
        stop_words = set(stopwords.words("english"))
    tokens = word_tokenize(str(text).lower())
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words]
    return " ".join(tokens)


def clean_texts(texts) -> list:
    """Vectorised clean_text for any iterable of strings.

    Stateless, so it is safe to use as the first step of a scikit-learn
    Pipeline (through FunctionTransformer) without causing leakage.
    """
    stop_words = set(stopwords.words("english"))
    return [clean_text(t, stop_words) for t in texts]


def load_and_clean(csv_path=DEFAULT_DATA_PATH) -> pd.DataFrame:
    """Load the raw CSV and return the cleaned, labelled DataFrame."""
    ensure_nltk_data()
    df = pd.read_csv(csv_path)
    df = df[KEEP_COLUMNS].dropna().drop_duplicates().reset_index(drop=True)
    df = df.rename(columns=RENAME_COLUMNS)
    df["Clean Review"] = clean_texts(df["Review Text"])
    df["Sentiment"] = df["Rating"].apply(get_sentiment)
    return df
