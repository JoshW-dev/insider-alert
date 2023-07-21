import yfinance as yf
import os
import pandas as pd

def get_stock_data(ticker, start_date, end_date):
    directory = 'stockData'
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    # Save the data to a CSV file
    stock_data.to_csv(f'{directory}/{ticker}_data.csv')
    return stock_data


