#  Orders & Customers Merge
#  Problem Name:
# Customer Order Integration
#  Description:
# Given:
# customers DataFrame
# orders DataFrame
# Merge them and compute:
# total spending per customer.

import numpy as np
import pandas as pd


def customer_order_integration(df1, df2):

    """
    customers DataFrame and orders DataFrame
    Merge them and compute: total spending per customer.
    """

    # Checking if its DataFrame or not
    if not isinstance(df1, pd.DataFrame) :
        df1 = pd.DataFrame(df1)

    if not isinstance(df2, pd.DataFrame) :
        df2 = pd.DataFrame(df2)

    # Merge the date
    df = pd.merge(df1, df2, on="CustomerID", how="left")
    
    
    # Add the total_spending to the table
    summary = df.groupby(["CustomerID", "Name"]).agg(
        total_spending=("Amount", "sum")
    ).reset_index()
    summary["total_spending"] = summary["total_spending"].fillna(0)

    return summary

# Create Data


# Random seed for reproducibility
np.random.seed(42)

# Customers DataFrame
customers = {
    "CustomerID": [1, 2, 3, 4, 5],
    "Name": ["Ahmed", "Sara", "Omar", "Laila", "Hassan"]
}


# Orders DataFrame
orders = {
    "OrderID": range(101, 111),  # 10 orders
    "CustomerID": np.random.choice([1,2,3,4,5], 10),
    "Amount": np.random.randint(100, 1000, 10)  # random spending
}




if __name__ == "__main__":
    print("Customers Data before merge:")
    print(customers)

    print("\nOrders Data before merge:")
    print(orders)

    print("\nThe data after merging customers and orders:")
    print(customer_order_integration(customers, orders))


# Output = >
# Customers Data before merge:
# {'CustomerID': [1, 2, 3, 4, 5], 'Name': ['Ahmed', 'Sara', 'Omar', 'Laila', 'Hassan']}

# Orders Data before merge:
# {'OrderID': range(101, 111), 'CustomerID': array([4, 5, 3, 5, 5, 2, 3, 3, 3, 5]), 
# 'Amount': array([199, 971, 763, 230, 761, 408, 869, 443, 591, 513], dtype=int32)}

# The data after merging customers and orders:
#    CustomerID    Name  total_spending
# 0           1   Ahmed             0.0
# 1           2    Sara           408.0
# 2           3    Omar          2666.0
# 3           4   Laila           199.0
# 4           5  Hassan          2475.0


