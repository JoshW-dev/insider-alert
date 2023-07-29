import scraper
import stockPrices
import pandas as pd
import visualize
import os
from datetime import datetime, timedelta

print("Main Script...")

#scrape web and save to insider_trades.csv
insiderUrl ='http://openinsider.com/latest-cluster-buys'
filename = "insider_trades"

print("Scraping OpenInsider Data")

#Scrape openinsider for cluster buys and save csv
scraper.scrape_insider_trades(insiderUrl,filename)
tickers = stockPrices.get_tickers_from_csv(filename)

#Scrape yahoo for ticker prices ove rpast 60 days 
print("Scraping Stock Prices")

stockPrices.save_stock_data(tickers)
print("Generating Price Graphs")
visualize.plot_multiple_stocks(tickers)

scraper.create_summary_file()