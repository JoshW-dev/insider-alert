import yfinance as yf
import os
import pandas as pd
from datetime import datetime, timedelta


def get_tickers_from_csv(fileName):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(fileName + ".csv")
    # Extract the ticker symbols
    tickers = df['Ticker'].unique()[:20].tolist()
    return tickers

def get_stock_data(ticker, start_date, end_date):
    directory = 'stockData'
    print("Getting stock data for " + ticker)
    print("From " + start_date + " to "+ end_date)
    
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    # Save the data to a CSV file
    stock_data.to_csv(f'{directory}/{ticker}_data.csv')
    return stock_data

def save_stock_data(tickers):
    # Loop over the tickers and download the stock data for each one
    for ticker in tickers:
        # Get the trade dates for the ticker
        trade_dates, _ = get_insider_dates(ticker)

        # Set the initial start date as 10 days before the first trade date
        start_date = trade_dates.min() - timedelta(days=10)

        # Calculate the end date (today)
        end_date = datetime.now().date()

        # Calculate the latest possible start date (30 days ago from today)
        latest_start_date = end_date - timedelta(days=30)

        # If the initial start date is within 30 days of the end date, set the start date as 30 days ago
        if (end_date - start_date).days < 30:
            start_date = latest_start_date

        # Download and save the stock data
        get_stock_data(ticker, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))





def combine_csv_files(directory):
    # Create a list to store the data from each CSV file
    data_list = []
    # Get a list of all CSV files in the directory
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    # Read each CSV file and add it to the list
    for file in csv_files:
        data = pd.read_csv(f'{directory}/{file}')
        data_list.append(data)
    # Combine all the data into one DataFrame
    combined_data = pd.concat(data_list)
    # Save the combined data to a CSV file
    combined_data.to_csv(f'{directory}/combined_data.csv', index=False)

def get_insider_dates(ticker, file_path='insider_trades.csv'):
    df = pd.read_csv(file_path)
    # Filter the DataFrame for the given ticker
    ticker_data = df[df['Ticker'] == ticker]

    # Extract the trade and filing dates
    trade_date = pd.to_datetime(ticker_data['Trade\xa0Date']).dt.date
    filing_date = pd.to_datetime(ticker_data['Filing\xa0Date']).dt.date

    return trade_date, filing_date
