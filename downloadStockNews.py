import yfinance as yf
from datetime import datetime

def download_stock_news(symbol):
    # Create a ticker object
    ticker = yf.Ticker(symbol)

    # Get news
    news = ticker.news

    # Save to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"stock_news_{symbol}_{timestamp}.txt"

    with open(filename, 'w', encoding='utf-8') as f:
        for article in news:
            f.write(f"Title: {article['title']}\n")
            f.write(f"Publisher: {article['publisher']}\n")
            f.write(f"Link: {article['link']}\n")
            f.write(f"Published: {article['providerPublishTime']}\n")
            f.write("-" * 50 + "\n")

    print(f"News saved to {filename}")

# Usage
symbol = "AAPL"  # Example: Apple stock
download_stock_news(symbol)

