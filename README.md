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

## Trading Strategy

Check if 2 or more company insiders have purchased more than $25k worth of stock on the same day
if
- insiders are not new
- avg volume in cash is >$10M 
- avg volume in cash is <$50M
