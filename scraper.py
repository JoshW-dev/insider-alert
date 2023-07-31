import requests
from bs4 import BeautifulSoup
import pandas as pd
import yfinance as yf

def scrape_insider_trades(url, fileName):
    # Download the webpage
    response = requests.get(url)
    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the table
    table = soup.find("table", {"class": "tinytable"})
    # Extract rows and columns
    data = []
    headers = [header.text for header in table.find_all('th')]
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if columns:
            data.append([column.text.strip() for column in columns])
        # Create DataFrame
    df = pd.DataFrame(data, columns=headers)
    
    # Remove symbols from numeric columns
    for col in df.columns:
        df[col] = df[col].str.replace('$', '')  # Remove dollar sign
        df[col] = df[col].str.replace('+', '')  # Remove plus sign
        df[col] = df[col].str.replace(',', '')  # Remove comma
        df[col] = df[col].str.replace('%', '')  # Remove percentage sign

    # Save to CSV
    df.to_csv(fileName+'.csv', index=False)

def create_summary_file():
    # Load the data
    insider_trades = pd.read_csv('insider_trades.csv')
    # Sort by 'Filing Date' and select the most recent 15 stocks
    insider_trades = insider_trades.sort_values('Filing\xa0Date', ascending=False).head(15)
    # Initialize an empty list to store the rows for the summary DataFrame
    rows = []

    for _, row in insider_trades.iterrows():
        try:
            # Create a Ticker object for the current ticker
            company = yf.Ticker(row['Ticker'])
            company_info = company.info
        except Exception as e:
            print(f"Error fetching data for {row['Ticker']}: {e}")
            company_info = {}

        row_dict = {
            'Filing Date': row['Filing\xa0Date'],
            'Trade Date': row['Trade\xa0Date'],
            'Ticker': row['Ticker'],
            'Company Name': row['Company\xa0Name'],
            'Industry': row['Industry'],
            'Ins': row['Ins'],
            'Price': row['Price'],
            'Qty': row['Qty'],
            'Owned': row['Owned'],
            'ΔOwn': row['ΔOwn'],
            'Value': row['Value'],
            'Yahoo Link': 'https://finance.yahoo.com/quote/' + row['Ticker'],
            'OpenInsider Link': 'http://openinsider.com/' + row['Ticker'],
            'Graph Image Name': row['Ticker'] + '_graph.png',
            'Stock Price CSV File Link': row['Ticker'] + '_data.csv',
            'Company Industry': company_info.get('industry', 'N/A'),
            'Company Employees': company_info.get('fullTimeEmployees', 'N/A'),
            'Company Average Volume': company_info.get('averageVolume', 'N/A'),
            'Company Market Cap': company_info.get('marketCap', 'N/A'),
            'Company Trailing PE': company_info.get('trailingPE', 'N/A'),
            'Company Forward PE': company_info.get('forwardPE', 'N/A'),
            'Company Dividend Yield': company_info.get('dividendYield', 'N/A'),
            'Company Profit Margins': company_info.get('profitMargins', 'N/A'),
            'Company Return on Equity': company_info.get('returnOnEquity', 'N/A'),
        }

        # Append the row dictionary to the rows list
        rows.append(row_dict)

    # Create the summary DataFrame
    summary = pd.DataFrame(rows)

    # Write the summary DataFrame to the summary.csv file
    summary.to_csv('summary.csv', index=False)


