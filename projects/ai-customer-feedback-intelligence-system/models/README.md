# Models

Trained models are **not** committed to Git. Re-create them from the code:

```bash
python -m src.train --data "data/Womens Clothing E-Commerce Reviews.csv"
```

This writes `models/sentiment_pipeline.joblib`: a scikit-learn `Pipeline` that contains the text cleaning step, the TF-IDF vectorizer (fitted on training data only) and the classifier. It accepts **raw review text**:

```python
import joblib
pipe = joblib.load("models/sentiment_pipeline.joblib")   # run from the repository root
pipe.predict(["The fabric feels cheap and the size runs very small."])
```

> **Security note:** `joblib` / `pickle` files can execute code when loaded. Only load model files that you created yourself or that come from a source you trust.

If you want to share a ready-made model, publish it through GitHub Releases or external storage and add the download link and a checksum here.
