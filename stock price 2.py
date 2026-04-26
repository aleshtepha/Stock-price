import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Stock Prices Data Set.csv")

# Time Analysis

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Check columns
print(df.columns)


# Filter data
apple = df[df['symbol'] == 'AAPL']
apple = apple.sort_values('date')

print(apple)

plt.plot(apple['date'], apple['close'])
plt.title("AAPL Stock Price Over Time")
plt.show()

apple['MA_30'] = apple['close'].rolling(window=30).mean()

plt.plot(apple['date'], apple['close'], label='Close')
plt.plot(apple['date'], apple['MA_30'], label='30-day MA')
plt.title('Stock Price vs 30-Day Moving Average')
plt.legend()
plt.show()