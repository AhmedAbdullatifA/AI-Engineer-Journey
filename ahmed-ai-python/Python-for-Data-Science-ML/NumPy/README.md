# NumPy Practice 🐍

A collection of NumPy exercises and mini-projects designed to build a strong foundation in **numerical computing, array manipulation, vectorization, broadcasting, boolean masking, and data preprocessing** using NumPy only.

The exercises progress from basic NumPy operations to more realistic data-analysis and machine-learning preprocessing tasks.

---

## 📚 Projects & Exercises

### 1. NumPy Basics & Array Manipulation

This exercise focuses on the fundamental building blocks of NumPy.

It covers:

* Creating arrays using `np.zeros()` and `np.ones()`
* Generating sequences with `np.arange()`
* Generating evenly spaced values with `np.linspace()`
* Creating identity matrices with `np.eye()`
* Generating random values with NumPy
* Reshaping arrays using `reshape()`
* Boolean indexing and filtering
* Matrix slicing and indexing
* Calculating sums and standard deviation
* Working with the `axis` parameter

### Main Concepts

* NumPy arrays
* Array creation
* Indexing & slicing
* Reshaping
* Boolean indexing
* Aggregation functions
* Axis-based operations
* Random number generation

---

## 2. Student Grades Analysis 🎓

A NumPy-based student performance analysis project.

The dataset contains the grades of **10 students across 5 subjects**.

The program analyzes the dataset to determine:

* Average grade for each student
* Average grade for each subject
* Student with the highest average
* Subject with the highest average
* Students whose average grade is at least 80
* Students who scored at least 60 in every subject
* Overall average grade
* Letter-grade classification for every grade

### Grade Classification

| Grade | Range    |
| ----- | -------- |
| A     | 90+      |
| B     | 80–89    |
| C     | 70–79    |
| D     | 60–69    |
| F     | Below 60 |

### Main Concepts

* `mean()`
* `axis`
* `argmax()`
* Boolean indexing
* `all()`
* `where()`
* Nested vectorized conditions
* 2D array manipulation

This project emphasizes understanding the difference between operations performed **across rows and across columns**.

---

## 3. Min-Max Feature Scaling 📊

This project implements **Min-Max normalization from scratch using NumPy only**.

Each column represents a feature, and each row represents a data sample.

The following formula is used:

```text
X_scaled = (X - X_min) / (X_max - X_min)
```

The result scales each feature to a range between **0 and 1**.

### Special Case

If a feature has no variance:

```text
X_max - X_min = 0
```

the implementation avoids division by zero by safely replacing the denominator with `1`.

### Main Concepts

* Feature scaling
* Normalization
* `min()`
* `max()`
* Broadcasting
* Vectorized arithmetic
* Handling zero-variance features

### Machine Learning Connection

Min-Max scaling is a common preprocessing technique used before applying many machine learning algorithms.

This exercise demonstrates how such preprocessing can be implemented **from scratch without using Scikit-learn**.

---

## 4. Standardization / Z-Score Normalization 📈

This project implements **feature standardization from scratch using NumPy only**.

Each feature is transformed using the standard score formula:

```text
X_normalized = (X - mean) / standard_deviation
```

After standardization, each feature has approximately:

```text
Mean = 0
Standard Deviation = 1
```

### Special Case

If a feature has a standard deviation of zero, the implementation safely prevents division by zero.

### Main Concepts

* Standardization
* Z-score normalization
* Mean and standard deviation
* Broadcasting
* Vectorized operations
* Zero-variance handling

### Machine Learning Connection

Standardization is an important preprocessing technique, especially for algorithms that are sensitive to feature scale.

---

## 5. Transaction Outlier Detection 💰

A more advanced NumPy mini-project that analyzes financial transaction data collected over **12 days**, with **6 transactions per day**.

The project detects unusually large transaction values and creates a cleaned version of the dataset.

### Outlier Detection

An observation is considered an outlier when:

```text
|x - mean| > 2 × standard_deviation
```

The project performs the following operations:

1. Calculate the average transaction value for each day.
2. Calculate the average value of each transaction position across all days.
3. Calculate the overall mean and standard deviation.
4. Detect outliers using the given statistical rule.
5. Create a Boolean mask identifying outlier positions.
6. Extract all detected outlier values.
7. Calculate the mean of all non-outlier values.
8. Replace every outlier with the non-outlier mean.
9. Store the result in `cleaned_transactions`.
10. Recalculate daily averages after cleaning.
11. Compare daily averages before and after cleaning.
12. Identify the day with the largest decrease.
13. Calculate the percentage change for every day.
14. Produce the final cleaned dataset with the same shape as the original.

### Main Concepts

* Statistical outlier detection
* Mean and standard deviation
* Boolean masks
* Boolean indexing
* `np.where()`
* `np.argmax()`
* Vectorized operations
* Array aggregation
* Data cleaning
* Percentage change
* Multi-dimensional array analysis

### Result

The dataset contains two detected outliers:

```text
[500, 500]
```

These values are replaced with the mean of the non-outlier transactions:

```text
126.18571428571428
```

The largest decrease in the daily average occurs on:

```text
Day 3
```

The project demonstrates how NumPy can be used to perform a complete small-scale **data cleaning and outlier detection workflow without Pandas or Scikit-learn**.

---

# 🧠 Skills Practiced

Across these exercises, the main NumPy concepts practiced include:

* Array creation
* Array shapes and dimensions
* Indexing and slicing
* Boolean indexing
* Boolean masks
* Vectorization
* Broadcasting
* Aggregation functions
* `axis=0` and `axis=1`
* `mean()`
* `std()`
* `min()`
* `max()`
* `sum()`
* `argmax()`
* `where()`
* `all()`
* `reshape()`
* Random number generation
* Feature scaling
* Feature standardization
* Outlier detection
* Data cleaning

---

# 🚫 Constraints

The advanced exercises were intentionally implemented under the following restrictions:

* **NumPy only**
* No Pandas
* No SciPy
* No Statistics module
* No Scikit-learn
* No `for` loops
* No `while` loops
* No explicit iteration

The goal is to solve the problems using **vectorized NumPy operations** instead of traditional Python iteration.

---

# 🎯 Learning Goals

The purpose of this collection is not simply to memorize NumPy functions.

The main goal is to develop the ability to:

1. Think in terms of arrays instead of individual values.
2. Understand how `axis` affects calculations.
3. Use Boolean masks to filter and manipulate data.
4. Replace explicit loops with vectorized operations.
5. Understand broadcasting and how NumPy performs element-wise operations.
6. Implement common data preprocessing techniques from scratch.
7. Apply NumPy to realistic data-analysis problems.
8. Build a foundation for future work with **Pandas, Machine Learning, and Data Engineering**.

---

# 🛠️ Technologies

* **Python**
* **NumPy**

---

# 📁 Suggested Structure

```text
NumPy/
│
├── README.md
│
├── numpy_basics.py
├── student_grades_analysis.py
├── min_max_scaling.py
├── standardization.py
└── transaction_outlier_detection.py
```

---

# 🚀 Progression

The exercises are organized from basic to more advanced concepts:

```text
NumPy Basics
     ↓
Array Manipulation
     ↓
Student Grades Analysis
     ↓
Feature Scaling
     ↓
Standardization
     ↓
Transaction Outlier Detection
```

This progression moves from basic array operations toward concepts commonly used in **data preprocessing and machine learning workflows**.
