import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# TODO 1. Get the stock Price and calculate the difference percent

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
close_prices = [float(value["4. close"]) for value in data_list]

diff_percent = (close_prices[0] - close_prices[1]) / close_prices[1] * 100

# TODO 2. Get the news articles if diff_percent is high

if abs(diff_percent) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"][:3]

    new_article = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in articles]
    print(new_article[0])
