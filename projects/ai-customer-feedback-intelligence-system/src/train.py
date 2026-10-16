"""Train and evaluate the sentiment classifiers.

Usage (from the repository root):
    python -m src.train --data "data/Womens Clothing E-Commerce Reviews.csv"

The train/test split happens BEFORE TF-IDF, so the vocabulary and IDF
weights are learned from training reviews only (no test-set leakage).
"""
import argparse
from pathlib import Path

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer

from src.clustering import cluster_negative_reviews, top_terms_per_cluster
from src.evaluate import evaluate_model, save_confusion_matrix, save_metrics
from src.preprocessing import DEFAULT_DATA_PATH, clean_texts, load_and_clean

RANDOM_STATE = 42


def build_models() -> dict:
    return {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Logistic Regression (balanced)": LogisticRegression(
            max_iter=1000, class_weight="balanced"
        ),
        "Random Forest": RandomForestClassifier(
            n_estimators=100, random_state=RANDOM_STATE, n_jobs=-1
        ),
        "Random Forest (balanced)": RandomForestClassifier(
            n_estimators=100, random_state=RANDOM_STATE, n_jobs=-1,
            class_weight="balanced",
        ),
    }


def main(data_path, models_dir, outputs_dir, final_model) -> None:
    models_dir, outputs_dir = Path(models_dir), Path(outputs_dir)
    models_dir.mkdir(parents=True, exist_ok=True)

    df = load_and_clean(data_path)
    print(f"Cleaned dataset: {df.shape[0]:,} reviews")

    # 1) split FIRST ...
    X_train_text, X_test_text, y_train, y_test = train_test_split(
        df["Clean Review"], df["Sentiment"],
        test_size=0.2, random_state=RANDOM_STATE, stratify=df["Sentiment"],
    )
    # 2) ... then learn vocabulary / IDF from the training split only.
    vectorizer = TfidfVectorizer(max_features=5000)
    X_train = vectorizer.fit_transform(X_train_text)
    X_test = vectorizer.transform(X_test_text)
    print("Train:", X_train.shape, "Test:", X_test.shape)

    rows, fitted = [], {}
    for name, model in build_models().items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        rows.append(evaluate_model(name, y_test, pred))
        save_confusion_matrix(name, y_test, pred, outputs_dir / "figures")
        fitted[name] = model
        print(f"  trained {name}")

    table = save_metrics(rows, outputs_dir / "model_metrics.csv")
    print(table[["model", "accuracy", "macro_f1", "recall_negative", "recall_neutral"]])

    # Inference pipeline that accepts RAW review text (cleaning included).
    pipeline = Pipeline(
        [
            ("clean", FunctionTransformer(clean_texts)),
            ("tfidf", vectorizer),
            ("clf", fitted[final_model]),
        ]
    )
    joblib.dump(pipeline, models_dir / "sentiment_pipeline.joblib")
    print(f"Saved inference pipeline ({final_model}) -> {models_dir}")

    # Complaint clustering (uses the vectorizer fitted on training data).
    negative, _ = cluster_negative_reviews(df, vectorizer, n_clusters=5)
    summary = top_terms_per_cluster(negative, vectorizer)
    summary.to_csv(outputs_dir / "cluster_summary.csv", index=False)
    print(summary)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", default=str(DEFAULT_DATA_PATH))
    parser.add_argument("--models-dir", default="models")
    parser.add_argument("--outputs-dir", default="outputs")
    parser.add_argument(
        "--final-model", default="Logistic Regression", choices=list(build_models())
    )
    args = parser.parse_args()
    main(args.data, args.models_dir, args.outputs_dir, args.final_model)
