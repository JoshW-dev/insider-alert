import requests
from bs4 import BeautifulSoup
import pandas as pd

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
    # Create the summary DataFrame
    summary = pd.DataFrame({
        'Filing Date': insider_trades['Filing\xa0Date'],
        'Trade Date': insider_trades['Trade\xa0Date'],
        'Ticker': insider_trades['Ticker'],
        'Company Name': insider_trades['Company\xa0Name'],
        'Industry': insider_trades['Industry'],
        'Ins': insider_trades['Ins'],
        'Price': insider_trades['Price'],
        'Qty': insider_trades['Qty'],
        'Owned': insider_trades['Owned'],
        'ΔOwn': insider_trades['ΔOwn'],
        'Value': insider_trades['Value'],
        'Yahoo Link': 'https://finance.yahoo.com/quote/' + insider_trades['Ticker'],
        'OpenInsider Link': 'http://openinsider.com/' + insider_trades['Ticker'],
        'Graph Image Name': insider_trades['Ticker'] + '_graph.png',
        'Stock Price CSV File Link': insider_trades['Ticker'] + '_data.csv'
    })
    # Write the summary DataFrame to the summary.csv file
    summary.to_csv('summary.csv', index=False)
