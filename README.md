# Insider Trading Alert Bot
This project is a bot designed to track and alert users when multiple high-level insiders (CEOs, CFOs, etc.) buy their own company's stock on the same day. This repository contains lightweight code for a Flask application that scrapes data and displays it on a webpage. The data is updated daily at 7 am EST.

Inspired by [this video](https://www.youtube.com/watch?v=bhxblVMqsbo) by Calum Shallenberger

## Live Site
You can view the live site at http://joshwdev.pythonanywhere.com/.


### Planned features:
- Send notifications via twilio when the specified trading activity is detected.
- Scrape additional stock info
- Optimize searched insider trends by back testing past trades
- Set up chatbot to answer questions about stocks and trading

## Project Structure
- app.py: This is the main Flask application file. It reads data from a CSV file and passes it to the home.html template.
- main.py: This script scrapes data fom http://openinsider.com/ and saves it as a CSV file.
- templates/home.html: This is the HTML template for the homepage. It displays the data in a table format.


## Running this app
This bot is hosted on [PythonAnywhere](http://joshwdev.pythonanywhere.com/), if you wish to run it locally, you can 
follow steps below

1. Clone the repository: 
```
git clone https://github.com/JoshWDev/insider-alert.git
```
2. Navigate to the project directory and install the required packages:
```
cd insider-alert
pip install -r requirements.txt
```

3. Run the Flask application: 
```
python app.py
```

## Running the webscraper Bot

After installing the dependencies, you can run the bot with the following command:

```
python main.py
```

The bot will scrape the recent insider trading data from OpenInsider, check for the specified trading activity, and update the summary.csv file.



## Insider Trading

Insider trading refers to the use of non-public information to make stock trading decisions. It's illegal if it involves material non-public information that can impact a company's stock price. However, it's legal for company insiders to trade their own company's stocks, as long as these trades are reported to the SEC in a timely manner. This information is publicly accessible, promoting market transparency.

This transparency is beneficial for non-insiders as it provides them with valuable insights into the actions of insiders who have deep knowledge of the company. By observing and analyzing these reported trades, non-insiders can potentially discern patterns or trends about the company's financial health, aiding their investment decisions. It also helps maintain a fair marketplace, as it discourages illegal activities and encourages equal access to information.

## Trading Strategy

Check if 2 or more company insiders have purchased more than $25k worth of stock on the same day
if
- insiders are not new
- avg volume in cash is >$10M 
- avg volume in cash is <$50M


## Contact
Let me know if you have any questions or feedback at joshuafwade@gmail.com
