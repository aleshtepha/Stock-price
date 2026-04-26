import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("2) Stock Prices Data Set.csv")

print(df.head())

print(df.columns)

# Check missing values
print(df.isnull().sum())

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Remove duplicates
df.drop_duplicates()

# check data types
print(df.dtypes)

# Exploratory Data Analysis (EDA)

print(df.describe())

# Example: Data distribution

df['open'].hist()
plt.title("Distribution of Opening Prices")
plt.show()

to