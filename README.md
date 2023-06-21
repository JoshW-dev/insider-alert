# Insider Trading Alert Bot
This project is a bot designed to track and alert users when multiple high-level insiders (CEOs, CFOs, etc.) buy their own company's stock on the same day. The bot scrapes data from OpenInsider and sends notifications when the specified trading activity is detected.

Inspired by [this video](https://www.youtube.com/watch?v=bhxblVMqsbo) by Calum Shallenberger

## Getting Started
Dependencies
The bot is implemented in Python and requires the following libraries:


- BeautifulSoup: for web scraping
- requests: for making HTTP requests
- pandas: for data manipulation
- smtplib: for sending emails (optional, if email notifications are desired)
- twilio: for sending text messages (optional, if SMS notifications are desired)

Install the dependencies with pip:


sh

```
pip install -r requirements.txt
```
For optional email and text message notifications:

```
pip install smtplib twilio
```

## Running the Bot

After installing the dependencies, you can run the bot with the following command:

```
python main.py
```

The bot will scrape the recent insider trading data from OpenInsider, check for the specified trading activity, and send notifications if any is found.

## Setting Up Notifications
To use the email and/or text message notifications, you'll need to provide some additional information in the script:

For email notifications, you'll need to provide the SMTP server and port, the email address and password to send from, and the recipient email address(es).

For text message notifications, you'll need to provide your Twilio account SID and auth token, the Twilio phone number to send from, and the recipient phone number(s).

Please replace the placeholders in the script with your actual information.

## Insider Trading

Insider trading refers to the use of non-public information to make stock trading decisions. It's illegal if it involves material non-public information that can impact a company's stock price. However, it's legal for company insiders to trade their own company's stocks, as long as these trades are reported to the SEC in a timely manner. This information is publicly accessible, promoting market transparency.

This transparency is beneficial for non-insiders as it provides them with valuable insights into the actions of insiders who have deep knowledge of the company. By observing and analyzing these reported trades, non-insiders can potentially discern patterns or trends about the company's financial health, aiding their investment decisions. It also helps maintain a fair marketplace, as it discourages illegal activities and encourages equal access to information.

## Trading Strategy

Check if 2 or more company insiders have purchased more than $25k worth of stock on the same day
if
- insiders are not new
- avg volume in cash is >$10M 
- avg volume in cash is <$50M
