# Multi-Table Business Join
# Problem Name:
# Retail Data Integration Pipeline
# Description:
# Given:
# customers
# orders
# products
# Merge all tables and compute:
# revenue per customer
# revenue per product category
# top 5 customers

import numpy as np
import pandas as pd


def retail_data_integration_pipeline(df1, df2 , df3):

    """
    Given: customers ,orders and products
    Merge all tables and compute: revenue per customer,
    revenue per product category,
    and top 5 customers
    """

    # Checking if its DataFrame or not
    if not isinstance(df1, pd.DataFrame) :
        df1 = pd.DataFrame(df1)

    if not isinstance(df2, pd.DataFrame) :
        df2 = pd.DataFrame(df2)

    if not isinstance(df3, pd.DataFrame) :
        df3 = pd.DataFrame(df3)

    # Merge the date
    df = pd.merge(df1, df2, on="CustomerID", how="left")
    df = pd.merge(df, df3, on="ProductID", how="left")
    
    
    # Add the total_revenue per customer to and product category
    df["revenue"] = df["Price"] * df["Quantity"]
    summary1 = df.groupby(["CustomerID"]).agg(
        total_revenue=("revenue", "sum")
    ).reset_index().fillna(0)


    summary2 = df.groupby(["Category"]).agg(
        total_revenue=("revenue", "sum")
    ).reset_index().fillna(0)


    top_customers = summary1.sort_values(by="total_revenue", ascending=False).head(5)

    return f"Revenue per customer:\n{summary1}\n\nRevenue per product category:\n{summary2}\n\nTop 5 customers:\n{top_customers}"

# Create Data


# Random seed for reproducibility
np.random.seed(42)

# Customers DataFrame
customers = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4, 5, 6, 7],
    "Name": ["Ahmed", "Sara", "Omar", "Laila", "Hassan", "Fatima", "Youssef"]
})


# Products DataFrame
products = pd.DataFrame({
    "ProductID": [101, 102, 103, 104],
    "ProductName": ["Laptop", "Phone", "Tablet", "Headphones"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories"],
    "Price": [800, 500, 300, 100]
})

# Orders DataFrame
orders = pd.DataFrame({
    "OrderID": range(1001, 1016),  # 15 orders
    "CustomerID": np.random.choice(customers["CustomerID"], 15),
    "ProductID": np.random.choice(products["ProductID"], 15),
    "Quantity": np.random.randint(1, 5, 15)  # 1–4 items per order
})




if __name__ == "__main__":
    print("Customers Data before merge:")
    print(customers)

    print("\nOrders Data before merge:")
    print(orders)

    print("\nProducts Data before merge:")
    print(products)

    print("\nRetail Data Integration Pipeline Results:")
    print(retail_data_integration_pipeline(customers, orders, products))


# Output = >
# Customers Data before merge:
#    CustomerID     Name
# 0           1    Ahmed
# 1           2     Sara
# 2           3     Omar
# 3           4    Laila
# 4           5   Hassan
# 5           6   Fatima
# 6           7  Youssef

# Orders Data before merge:
#     OrderID  CustomerID  ProductID  Quantity
# 0      1001           7        104         4
# 1      1002           4        104         2
# 2      1003           5        103         2
# 3      1004           7        102         1
# 4      1005           3        101         4
# 5      1006           5        102         1
# 6      1007           5        104         1
# 7      1008           7        104         3
# 8      1009           2        102         3
# 9      1010           3        102         3
# 10     1011           7        102         2
# 11     1012           3        104         4
# 12     1013           3        104         4
# 13     1014           5        101         4
# 14     1015           4        101         4

# Products Data before merge:
#    ProductID ProductName     Category  Price
# 0        101      Laptop  Electronics    800
# 1        102       Phone  Electronics    500
# 2        103      Tablet  Electronics    300
# 3        104  Headphones  Accessories    100

# Retail Data Integration Pipeline Results:
# Revenue per customer:
#    CustomerID  total_revenue
# 0           1            0.0
# 1           2         1500.0
# 2           3         5500.0
# 3           4         3400.0
# 4           5         4400.0
# 5           6            0.0
# 6           7         2200.0

# Revenue per product category:
#       Category  total_revenue
# 0  Accessories         1800.0
# 1  Electronics        15200.0

# Top 5 customers:
#    CustomerID  total_revenue
# 2           3         5500.0
# 4           5         4400.0
# 3           4         3400.0
# 6           7         2200.0
# 1           2         1500.0

