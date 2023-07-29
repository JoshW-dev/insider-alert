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

