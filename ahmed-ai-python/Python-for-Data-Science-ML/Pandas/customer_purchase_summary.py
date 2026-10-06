# Customer Spending Report
# Problem Name:
# Customer Purchase Summary
# Description:
# Given transactions DataFrame:
# Group by customer.
# Calculate:
# total spending
# average purchase
# number of transactions
# the diffrence between the high and low value 

import numpy as np
import pandas as pd


def customer_purchase_summary(df):

    """
    Given transactions DataFrame: 
    Group by customer.
    Calculate:
    total spending
    average purchase
    number of transactions
    the diffrence between the high and low value 
    """

    # Checking if its DataFrame or not
    if not isinstance(df, pd.DataFrame) :
        df = pd.DataFrame(df)

    # do the requrments :
    summary = df.groupby("Customer").agg(
    total_spending=("Amount", "sum"),
    average_purchase=("Amount", "mean"),
    num_transactions=("Amount", "count"),
    range_spending=("Amount", lambda x: x.max() - x.min())
    )
    
    return summary


# Create Data

# Create random dataset
np.random.seed(42)  # for reproducibility

# Generate 50 random transactions 
d = {
    "Customer": np.random.choice(["Ahmed", "Mohammed", "Omar", "Hazem", "Noha"], 50),
    "Amount": np.random.randint(1, 1000, 50)  # random spending between 1–1000
}

df = pd.DataFrame(d)


if __name__ == "__main__":

    print("Transactions Data before summary:")
    print(df)

    print("Customer Purchase Summary after calculations:")
    print(customer_purchase_summary(df))



# output =>    
# Transactions Data before summary:
#     Customer  Amount
# 0      Hazem      92
# 1       Noha     367
# 2       Omar     956
# 3       Noha     455
# 4       Noha     428
# 5   Mohammed     509
# 6       Omar     776
# 7       Omar     943
# 8       Omar      35
# 9       Noha     206
# 10     Hazem      81
# 11      Omar     932
# 12      Noha     562
# 13  Mohammed     872
# 14     Hazem     388
# 15  Mohammed       2
# 16     Hazem     390
# 17      Noha     566
# 18     Ahmed     106
# 19     Hazem     772
# 20  Mohammed     822
# 21      Noha     477
# 22     Hazem     703
# 23     Ahmed     402
# 24     Ahmed     730
# 25      Omar     556
# 26      Omar     162
# 27  Mohammed     202
# 28     Hazem     958
# 29     Hazem     996
# 30      Omar     270
# 31     Hazem     863
# 32     Hazem     816
# 33     Ahmed     271
# 34      Omar     456
# 35      Noha     462
# 36      Omar     727
# 37      Noha     252
# 38     Ahmed     702
# 39  Mohammed     296
# 40     Hazem     725
# 41     Ahmed     720
# 42     Hazem     749
# 43  Mohammed     338
# 44  Mohammed     879
# 45     Ahmed      53
# 46  Mohammed     792
# 47      Noha     922
# 48  Mohammed     217
# 49     Hazem     764
# Customer Purchase Summary after calculations:
#           total_spending  average_purchase  num_transactions  range_spending
# Customer                                                                    
# Ahmed               2984        426.285714                 7             677
# Hazem               8297        638.230769                13             915
# Mohammed            4929        492.900000                10             877
# Noha                4697        469.700000                10             716
# Omar                5813        581.300000                10             921

