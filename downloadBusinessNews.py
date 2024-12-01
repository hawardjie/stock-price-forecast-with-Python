import requests
from datetime import datetime
import json
import os

def download_business_news():
    # You'll need to sign up for a free API key at newsapi.org
    API_KEY = ''

    # NewsAPI endpoint for business news
    url = 'https://newsapi.org/v2/top-headlines'

    # Parameters for the API request
    params = {
        'apiKey': API_KEY,
        'category': 'business',
        'language': 'en',
        'pageSize': 100  # Get up to 100 articles
    }

    try:
        # Make the API request
        response = requests.get(url, params=params)
        response.raise_for_status()

        # Parse the JSON response
        news_data = response.json()

        # Create filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'business_news_{timestamp}.txt'

        # Write the news to a file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Business News - Downloaded on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            for article in news_data.get('articles', []):
                f.write(f"Title: {article.get('title', 'No title')}\n")
                f.write(f"Source: {article.get('source', {}).get('name', 'Unknown source')}\n")
                f.write(f"Published: {article.get('publishedAt', 'No date')}\n")
                f.write(f"Description: {article.get('description', 'No description')}\n")
                f.write(f"Content: {article.get('content', 'No content')}\n")
                f.write("\n" + "-"*80 + "\n\n")

        print(f"News has been downloaded and saved to {filename}")

    except requests.RequestException as e:
        print(f"Error downloading news: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_business_news()

