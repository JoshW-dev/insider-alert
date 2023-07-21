import yfinance as yf
import os
import pandas as pd

def get_stock_data(ticker, start_date, end_date):
    directory = 'stockData'
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    # Save the data to a CSV file
    stock_data.to_csv(f'{directory}/{ticker}_data.csv')
    return stock_data


#most recent 10 cluster buys as of July 21

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