import os
import matplotlib.pyplot as plt
import pandas as pd
import stockPrices
import glob

def plot_stock_price(ticker):
    # Define the file path for the stock data CSV file
    file_path = f'stockData/{ticker}_data.csv'

    # Load the stock data into a pandas DataFrame
    stock_data = pd.read_csv(file_path)

    # Convert the 'Date' column to a datetime object
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])

    # Set the 'Date' column as the index
    stock_data.set_index('Date', inplace=True)

    # Create a line plot of the closing price over time
    plt.figure(figsize=(8, 6))
    plt.plot(stock_data['Close'], label='Close Price')
    plt.xticks(rotation=30)

  # Add a marker for the latest price
    latest_date = stock_data.index[-1]
    latest_price = stock_data['Close'].iloc[-1]
    plt.scatter(latest_date, latest_price, color='red')
    plt.annotate(f'{latest_date.strftime("%Y-%m-%d")}\n${latest_price:.2f}', 
                 (latest_date, latest_price), textcoords="offset points", xytext=(0,15),
                 verticalalignment='bottom', horizontalalignment='center', 
                 fontsize=10, fontweight='bold')

    # Get the insider trading dates
    trade_dates, filing_dates = stockPrices.get_insider_dates(ticker)
   # Add vertical lines and labels for the trade dates
    for trade_date in trade_dates:
        plt.axvline(x=trade_date, color='blue', linestyle='--', alpha=0.5)
        plt.annotate(f'Trade Date\n{trade_date.strftime("%Y-%m-%d")}',
                     (trade_date, stock_data['Close'].min()), textcoords="offset points", xytext=(0,60),
                     verticalalignment='top', horizontalalignment='right',
                     fontsize=10, color='blue')

    # Add vertical lines and labels for the filing dates
    for filing_date in filing_dates:
        plt.axvline(x=filing_date, color='green', linestyle='--', alpha=0.5)
        plt.annotate(f'Filing Date\n{filing_date.strftime("%Y-%m-%d")}',
                     (filing_date, stock_data['Close'].min()), textcoords="offset points", xytext=(0,0),
                     verticalalignment='bottom', horizontalalignment='left',
                     fontsize=10, color='green')

    plt.title(f'{ticker} Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.grid(True)

    # Create a directory for the graphs if it doesn't exist
    if not os.path.exists('graphs'):
        os.makedirs('graphs')

    # Save the graph as a PNG file in the 'graphs' directory
    plt.savefig(f'graphs/{ticker}_graph.png')
    



def plot_multiple_stocks(tickers):
    # Delete all .png files in the 'graphs' directory
    files = glob.glob('graphs/*.png')
    for f in files:
        os.remove(f)

    for ticker in tickers:
        plot_stock_price(ticker)