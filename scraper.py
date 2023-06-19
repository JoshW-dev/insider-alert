# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape(post_url):


    # Define the URL of the site
    base_url = 'http://openinsider.com/'
    print("Webscraping : " + base_url+post_url)

    # Send a GET request to the site
    response = requests.get(base_url+post_url)

    # Parse the content of the request with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table that contains the data
    table = soup.find('table', {'class': 'tinytable'})

    # Find the headers of the table and store them in a list
    headers = [header.text for header in table.find_all('th')]

    # Find all the rows in the table
    rows = table.find_all('tr')

    # Loop over the rows and get the data from each cell
    data = []
    for row in rows[1:]: # The first row is the headers, so skip it
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)

    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=headers)
    return df

