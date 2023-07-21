import pandas as pd
import matplotlib.pyplot as plt

def calculate_percentage_change(start_price, end_price):
    return ((end_price - start_price) / start_price) * 100


#cleaned stock data scraped from http://openinsider.com/latest-cluster-buys
data = pd.read_csv('insider_trades.csv')

# Load the combined stock data
combined_data = pd.read_csv('stockData/combined_data.csv')

# Convert the 'Date' column to datetime
combined_data['Date'] = pd.to_datetime(combined_data['Date'])

# Set the 'Date' column as the index
combined_data.set_index('Date', inplace=True)

# Get the trade dates for each ticker
trade_dates = {row['Unnamed: 3']: row['Unnamed: 2'] for _, row in data[1:11].iterrows()}
trade_dates = {ticker: pd.to_datetime(date) for ticker, date in trade_dates.items()}

# Get today's date
today = pd.to_datetime('2023-07-21')

# Calculate the percentage change in stock prices for each ticker
percentage_changes = {}
for ticker in combined_data['Ticker'].unique():
    ticker_data = combined_data[combined_data['Ticker'] == ticker]
    trade_date = trade_dates[ticker]
    trade_price = ticker_data.loc[trade_date, 'Close']
    # Get the latest available date if today's date is not available
    try:
        today_price = ticker_data.loc[today, 'Close']
    except KeyError:
        today_price = ticker_data['Close'].iloc[-1]
    percentage_change = calculate_percentage_change(trade_price, today_price)
    percentage_changes[ticker] = {
        'trade_price': trade_price,
        'today_price': today_price,
        'percentage_change': percentage_change
    }

# Plot the stock prices for each ticker over time in separate graphs
for ticker in combined_data['Ticker'].unique():
    plt.figure(figsize=(10, 5))
    ticker_data = combined_data[combined_data['Ticker'] == ticker]
    plt.plot(ticker_data.index, ticker_data['Close'], label=ticker)

    # Add an indicator for the trade date
    trade_date = trade_dates[ticker]
    trade_price = ticker_data.loc[trade_date, 'Close']
    plt.scatter(trade_date, trade_price, color='red')
    plt.text(trade_date, trade_price, f'Trade Date, {percentage_changes[ticker]["percentage_change"]:.2f}% change to latest', verticalalignment='bottom')

    plt.title(f'Stock Prices for {ticker} Over Time')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.grid(True)
    plt.show()

# Print the report
for ticker, info in percentage_changes.items():
    print(f'{ticker}:')
    print(f'  Trade price: {info["trade_price"]}')
    print(f'  Today\'s price: {info["today_price"]}')
    print(f'  Percentage change: {info["percentage_change"]:.2f}%')
    print()
