import requests
from datetime import date, timedelta
import os
from twilio.rest import Client
account_sid = "AC4aa59b263bd38ca010bd2fdd6f280cd8"
auth_token = "a83c46a61f31c1a922a8d911b46e1e02"
client = Client(account_sid, auth_token)


today = date.today()
# Get the news from the API
news_url = ('https://newsapi.org/v2/top-headlines?'
            'q=Tesla&'
            f'from={today}&'
            'language=en&'
            'sortBy=relevancy&'
            'apiKey=b0cce4a93a304c7dab515a65004838af')

news_api_response = requests.get(news_url)
news_response = news_api_response.json()
articles = news_response["articles"]
contents = [(article['title'], article['content']) for article in articles]

# Get the stock prices from the API
stock_price_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSCO&outputsize" \
                  "=compact&apikey=L0XTA027CS3XHVXH "

stock_price_api_response = requests.get(stock_price_url)
data = stock_price_api_response.json()
trading_symbol = data["Meta Data"]["2. Symbol"]
dates = [date for date in data["Time Series (Daily)"]]
before_yesterday_closing_price = float(data["Time Series (Daily)"][f"{dates[1]}"]["4. close"])
yesterday_closing_price = float(data["Time Series (Daily)"][f"{dates[0]}"]["4. close"])

# calculate the percentage change
percentage_change = ((yesterday_closing_price - before_yesterday_closing_price) / yesterday_closing_price * 100)

message = ""
for content in contents:
    if content[0] != "" and content[1] != "" and content[0] != None and content[1] != None:
        if percentage_change > 0:
            message += f"{trading_symbol} 🔺 {abs(round(percentage_change,3))}%\n"
        elif percentage_change < 0:
            message += f"{trading_symbol} 🔻 {abs(round(percentage_change,3))}%\n"
        message += f'Headline: {content[0]}\n'
        message += f'Breif: {content[1]}\n'

print(message)
msg = client.messages.create(
  body=message,
  from_="+15628372242",
  to="+251912677537"
)

