# Data

The dataset is **not** stored in this repository (size and licensing).

## How to get it

1. Download **Women's E-Commerce Clothing Reviews** (23,486 rows, 10 feature columns) from its original source on Kaggle (author: nicapotato).
2. Check the license on the source page before redistributing any part of it.
3. Save the file here with this exact name:

```
data/Womens Clothing E-Commerce Reviews.csv
```

## What the project creates locally

Running the notebook writes `data/processed/cleaned_customer_reviews.csv` (the cleaned reviews plus the derived `Clean Review` and `Sentiment` columns). It contains review text, so it is git-ignored and should not be pushed unless the dataset license allows redistribution.
