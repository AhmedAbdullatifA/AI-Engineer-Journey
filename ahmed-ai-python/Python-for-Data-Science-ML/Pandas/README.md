# 🐼 Pandas Practice

A collection of **Pandas exercises, data-analysis tasks, and Exploratory Data Analysis (EDA) projects** designed to build practical skills in working with structured and tabular data using Python.

This section of my Python-for-Data-Science journey focuses on **data inspection, filtering, aggregation, grouping, merging, missing-data handling, string operations, statistical analysis, and time-series analysis**.

The repository contains both **individual Pandas exercises** and **larger EDA projects** based on real-world-style datasets.

---

# 📚 Contents

This folder contains three main areas:

* **Pandas Exercises** — Practical problems focused on specific Pandas concepts.
* **Ecommerce Purchases Analysis** — An exploratory data analysis project containing 14 questions.
* **SF Salaries Exercise** — A salary dataset analysis containing 15 data-analysis questions.

---

# 🧩 Pandas Exercises

The exercises below focus on applying Pandas to practical data-analysis problems.

### 1. Customer Order Integration

Merges customer and order data using `CustomerID` and calculates the total spending for each customer.

**Main concepts:**

* `pd.merge()`
* Left joins
* `groupby()`
* Aggregation with `agg()`
* Handling customers with no orders
* DataFrame creation and transformation

---

### 2. Customer Purchase Summary

Analyzes customer transactions and produces a summary containing:

* Total spending
* Average purchase value
* Number of transactions
* Difference between the highest and lowest purchase

**Main concepts:**

* `groupby()`
* `agg()`
* `sum()`
* `mean()`
* `count()`
* Custom aggregation

---

### 3. Dataset Quick Summary Tool

A reusable function that loads a CSV dataset and provides a quick overview including:

* Number of rows and columns
* Data types
* Missing values
* Descriptive statistics

The exercise also demonstrates generating a small dataset and saving it to CSV.

**Main concepts:**

* `pd.read_csv()`
* `shape`
* `dtypes`
* `isnull().sum()`
* `describe()`
* `to_csv()`

---

### 4. Department Salary Analysis

Calculates the average salary for each department and identifies employees whose salary is above their department's average.

**Main concepts:**

* `groupby()`
* `transform()`
* Group-level calculations
* Boolean filtering
* Comparing individual rows with group statistics

---

### 5. Employee Performance Filter

Filters employees based on multiple business conditions:

* Salary above the company average
* Department contains more than 5 employees
* Performance score is above the 75th percentile

**Main concepts:**

* Multiple Boolean conditions
* `groupby().transform()`
* `mean()`
* `quantile()`
* Boolean indexing
* `&`

---

### 6. Hierarchical Sales Analysis

Analyzes sales data by **Region and Product**, calculating:

* Total revenue
* Average revenue
* Number of transactions

The results are then sorted by region and revenue.

**Main concepts:**

* Multi-column `groupby()`
* `agg()`
* `sum()`
* `mean()`
* `count()`
* Sorting

---

### 7. Mini Data Profiling System

Builds a small data-profiling system that analyzes each column according to its data type.

For numerical columns:

* Mean
* Standard deviation
* Minimum
* Maximum

For categorical columns:

* Number of unique values
* Top 3 most frequent values

**Main concepts:**

* Data-type detection
* `is_numeric_dtype()`
* `mean()`
* `std()`
* `min()`
* `max()`
* `nunique()`
* `value_counts()`
* Building structured DataFrames

---

### 8. Missing Data Sensitivity Analysis

Compares two approaches to missing numerical values:

1. Removing missing values
2. Filling missing values with the mean

The exercise compares how these approaches affect the resulting mean and standard deviation.

**Main concepts:**

* `dropna()`
* `fillna()`
* `mean()`
* `std()`
* Numeric type detection
* Comparing data-cleaning strategies

---

### 9. Retail Data Integration Pipeline

Integrates customer, order, and product datasets.

The analysis calculates:

* Revenue using `Price × Quantity`
* Revenue per customer
* Customer categories
* Top 5 customers

**Main concepts:**

* Multiple `merge()` operations
* Calculated columns
* `groupby()`
* Aggregation
* Sorting
* `head()`

---

### 10. Rolling Performance Tracker

Calculates a **3-period rolling average** and identifies values that are greater than twice their corresponding rolling average.

**Main concepts:**

* Pandas Series
* `rolling()`
* Rolling mean
* Boolean filtering
* Basic time-series analysis
* Anomaly identification

---

### 11. Monthly Sales Growth Analyzer

Analyzes monthly sales performance by calculating month-over-month percentage growth.

The analysis identifies:

* The month with the highest growth
* Months with negative growth

**Main concepts:**

* `pct_change()`
* `idxmax()`
* Boolean filtering
* Percentage calculations
* Time-series analysis

---

### 12. Smart Missing Value Handler

Automatically handles missing values according to column type:

* Numerical columns → filled with the mean
* Categorical columns → filled with the mode

**Main concepts:**

* `fillna()`
* `mean()`
* `mode()`
* `is_numeric_dtype()`
* Numerical vs categorical data
* Data cleaning

---

# 🛒 E-Commerce Purchases Analysis

An **Exploratory Data Analysis (EDA)** project based on an Ecommerce Purchases dataset using **Python and Pandas**.

The project contains **14 analysis questions** covering dataset inspection, descriptive statistics, filtering, grouping, string manipulation, time-based analysis, and credit-card-related analysis.

### Dataset

The project uses the `EcommercePurchases` dataset containing customer purchase information such as:

* Address
* Job
* Language
* Purchase Price
* Credit Card information
* Email
* Purchase time information

### Analysis Includes

* Dataset inspection
* DataFrame shape and structure
* Descriptive statistics
* Conditional filtering
* Job-title frequency analysis
* AM / PM purchase analysis
* Credit-card provider analysis
* Credit-card expiration analysis
* Email and domain analysis
* String manipulation
* Multiple-condition filtering
* Grouping and aggregation

### Key Questions

Examples of questions answered in the project include:

* What is the average purchase price?
* What are the highest and lowest purchase prices?
* How many users selected English as their language?
* How many users have the job title `Lawyer`?
* How many purchases occurred during AM and PM?
* What are the 5 most common job titles?
* What was the purchase price for a specific lot?
* How many American Express users made purchases above `$95`?
* How many credit cards expire in 2025?
* What are the most popular email providers?

### Project Files

```text
Ecommerce_Purchases_Analysis/
│
├── ecommerce_purchases_analysis.py
├── EcommercePurchases
└── README.md
```

📄 [View the Ecommerce Purchases README](./Ecommerce_Purchases_Analysis/README.md)

---

# 💰 SF Salaries Exercise

An exploratory **data-analysis exercise** based on the San Francisco Salaries dataset.

The project contains **15 analysis questions** covering dataset inspection, salary statistics, grouping, frequency analysis, string operations, filtering, and correlation analysis.

### Dataset

The dataset contains information including:

* Employee name
* Job title
* Base pay
* Overtime pay
* Other pay
* Benefits
* Total pay
* Total pay with benefits
* Year
* Agency
* Status

### Analysis Includes

* Dataset inspection with `head()` and `info()`
* Salary statistics
* Maximum and minimum salary analysis
* Employee lookup
* Grouped yearly salary analysis
* Unique job-title analysis
* Job-title frequency analysis
* String searching with `str.contains()`
* String-length analysis
* Correlation analysis

### Key Questions

Examples of questions answered in the project include:

* What is the average `BasePay`?
* What is the highest `OvertimePay`?
* What is the job title of a specific employee?
* How much does an employee make including benefits?
* Who is the highest-paid employee?
* Who is the lowest-paid employee?
* What is the average `BasePay` per year?
* How many unique job titles are there?
* What are the 5 most common jobs?
* How many job titles appeared only once in 2013?
* How many people have `Chief` in their job title?
* Is there a correlation between job-title length and salary?

### Project Files

```text
SF-Salaries-Exercise/
│
├── sf_salaries_exercise.py
├── Salaries.csv
└── README.md
```

📄 [View the SF Salaries README](./SF-Salaries-Exercise/README.md)

---

# 🧠 Skills Practiced

### Data Inspection

* `head()`
* `info()`
* `shape`
* `dtypes`
* `describe()`

### Data Selection & Filtering

* Boolean indexing
* Multiple conditions
* `&`
* `isin()`
* String filtering
* `str.contains()`

### Grouping & Aggregation

* `groupby()`
* `agg()`
* `transform()`
* `sum()`
* `mean()`
* `count()`
* `std()`
* `quantile()`

### Data Integration

* `merge()`
* Left joins
* Multi-table integration
* Calculated columns

### Missing Data

* `isnull()`
* `dropna()`
* `fillna()`
* Mean imputation
* Mode imputation

### Data Profiling

* Data-type detection
* `nunique()`
* `value_counts()`
* Descriptive statistics

### String & Text Operations

* `str.contains()`
* String length
* Email/domain extraction

### Time-Series Analysis

* `pct_change()`
* `rolling()`
* Rolling averages
* Growth analysis

### Statistical Analysis

* Mean
* Standard deviation
* Correlation
* Percentiles

---

# 🎯 Learning Goals

Through these exercises and projects, I am practicing how to:

1. Inspect and understand structured datasets.
2. Select and filter data using Pandas.
3. Perform grouped analysis and aggregations.
4. Compare individual values with group-level statistics.
5. Combine related datasets using joins and merges.
6. Handle missing data using different strategies.
7. Build reusable data-analysis functions.
8. Perform exploratory data analysis.
9. Analyze categorical and numerical data.
10. Work with strings and text-based columns.
11. Perform basic time-series analysis.
12. Apply statistical operations to real datasets.
13. Solve practical, business-oriented data-analysis problems.

---

# 🛠️ Technologies

* **Python**
* **Pandas**
* **NumPy**

---

# 📁 Project Structure

```text
Pandas/
│
├── Ecommerce_Purchases_Analysis/
│   ├── ecommerce_purchases_analysis.py
│   ├── EcommercePurchases
│   └── README.md
│
├── SF-Salaries-Exercise/
│   ├── sf_salaries_exercise.py
│   ├── Salaries.csv
│   └── README.md
│
├── customer_order_integration.py
├── customer_purchase_summary.py
├── dataset_quick_summary_tool.py
├── department_salary_analysis.py
├── employee_performance_filter.py
├── hierarchical_sales_analysis.py
├── mini_data_profiling_system.py
├── missing_data_sensitivity_analysis.py
├── retail_data_integration_pipeline.py
├── rolling_performance_tracker.py
├── sales_growth_analyzer.py
└── smart_missing_handler.py
```

---

# 🚀 Learning Progression

```text
Pandas Fundamentals
        ↓
Data Inspection
        ↓
Data Selection & Filtering
        ↓
GroupBy & Aggregation
        ↓
Group-Level Analysis
        ↓
Data Merging
        ↓
Multi-Table Integration
        ↓
Missing Data Handling
        ↓
Data Profiling
        ↓
String & Text Operations
        ↓
Exploratory Data Analysis
        ↓
Statistical Analysis
        ↓
Time-Series Analysis
```

---

# 📌 Learning Context

These exercises and projects are part of my broader **Python for Data Science & Machine Learning** learning journey.

The goal is to build a strong foundation in **data manipulation and analysis with Pandas** before progressing toward more advanced Data Science and Machine Learning workflows.

---

## 👨‍💻 Author

**Ahmed Abdullatif**

Computer Science & Artificial Intelligence Student

**Interests:** Python | SQL | Data Science | Machine Learning | AI
