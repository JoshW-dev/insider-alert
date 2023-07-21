import yfinance as yf
import os
import pandas as pd

def get_stock_data(ticker, start_date, end_date):
    directory = 'stockData'
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    # Add a column with the ticker symbol
    stock_data['Ticker'] = ticker
    # Save the data to a CSV file
    stock_data.to_csv(f'{directory}/{ticker}_data.csv')
    return stock_data

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


# The most recent 10 cluster buys as of July 21
ticker_date_ranges = [
    ('MLKN', '2023-06-18', '2023-07-21'),
    ('CAPIX', '2023-05-23', '2023-07-21'),
    ('CVGW', '2023-06-14', '2023-07-21'),
    ('CDZI', '2023-06-06', '2023-07-21'),
    ('EPSN', '2023-06-06', '2023-07-21'),
    ('CNXC', '2023-06-05', '2023-07-21'),
    ('KGS', '2023-06-03', '2023-07-21'),
    ('TURN', '2023-04-18', '2023-07-21'),
    ('OKE', '2023-05-29', '2023-07-21'),
    ('CMT', '2023-05-28', '2023-07-21')
]

for ticker, start_date, end_date in ticker_date_ranges:
    get_stock_data(ticker, start_date, end_date)

# Combine all the CSV files
combine_csv_files('stockData')
