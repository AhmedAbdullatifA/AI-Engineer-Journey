"""K-Means clustering of negative reviews into complaint themes."""
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def cluster_negative_reviews(df, vectorizer, n_clusters=5, random_state=42):
    """Cluster the Negative reviews using an already-fitted TF-IDF vectorizer.

    Returns (negative_df_with_cluster_column, fitted_kmeans).
    """
    negative = df[df["Sentiment"] == "Negative"].copy()
    X_neg = vectorizer.transform(negative["Clean Review"])
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=10)
    negative["Cluster"] = kmeans.fit_predict(X_neg)
    return negative, kmeans


def top_terms_per_cluster(negative, vectorizer, top_n=10) -> pd.DataFrame:
    """Top-N TF-IDF terms (by summed weight) and size of every cluster."""
    feature_names = vectorizer.get_feature_names_out()
    rows = []
    for cluster in sorted(negative["Cluster"].unique()):
        subset = negative[negative["Cluster"] == cluster]
        weights = np.asarray(
            vectorizer.transform(subset["Clean Review"]).sum(axis=0)
        ).ravel()
        top = weights.argsort()[-top_n:][::-1]
        rows.append(
            {
                "cluster": int(cluster),
                "reviews": len(subset),
                "share_of_negative": round(len(subset) / len(negative), 4),
                "top_terms": ", ".join(feature_names[top]),
            }
        )
    return pd.DataFrame(rows)


def silhouette_scan(negative, vectorizer, k_values=range(2, 9), random_state=42):
    """Silhouette score for several k, to sanity-check the choice of k=5."""
    X_neg = vectorizer.transform(negative["Clean Review"])
    scores = {}
    for k in k_values:
        labels = KMeans(n_clusters=k, random_state=random_state, n_init=10).fit_predict(X_neg)
        scores[k] = round(float(silhouette_score(X_neg, labels)), 4)
    return scores
