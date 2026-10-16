"""Metrics and plots for the sentiment classifiers."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
    f1_score,
)

LABELS = ["Negative", "Neutral", "Positive"]


def evaluate_model(name, y_true, y_pred) -> dict:
    """Return a flat dict of the metrics we report for one model."""
    report = classification_report(
        y_true, y_pred, labels=LABELS, output_dict=True, zero_division=0
    )
    row = {
        "model": name,
        "accuracy": accuracy_score(y_true, y_pred),
        "macro_f1": f1_score(y_true, y_pred, average="macro", zero_division=0),
    }
    for label in LABELS:
        row[f"recall_{label.lower()}"] = report[label]["recall"]
        row[f"precision_{label.lower()}"] = report[label]["precision"]
        row[f"f1_{label.lower()}"] = report[label]["f1-score"]
    return row


def save_confusion_matrix(name, y_true, y_pred, out_dir) -> Path:
    """Save a row-normalised confusion matrix as PNG and return its path."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(5.5, 4.5))
    ConfusionMatrixDisplay.from_predictions(
        y_true, y_pred, labels=LABELS, normalize="true",
        cmap="Blues", values_format=".2f", ax=ax,
    )
    ax.set_title(f"Confusion matrix - {name}")
    fig.tight_layout()
    safe = name.lower().replace(" ", "_").replace("(", "").replace(")", "")
    path = out_dir / f"confusion_matrix_{safe}.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def save_metrics(rows, path) -> pd.DataFrame:
    """Write the metrics table to CSV and return it."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    table = pd.DataFrame(rows).round(4)
    table.to_csv(path, index=False)
    return table
