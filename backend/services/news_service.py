
import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv(dotenv_path="config/.env")

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = "https://newsapi.org/v2/everything"

def fetch_news():
    # Define parameters for fetching news; adjust keywords as needed.
    keywords = "technology"  # Modify based on your industry focus
    today = datetime.utcnow()
    from_date = (today - timedelta(days=1)).strftime("%Y-%m-%d")
    to_date = today.strftime("%Y-%m-%d")
    
    params = {
        "q": keywords,
        "from": from_date,
        "to": to_date,
        "apiKey": NEWS_API_KEY,
        "sortBy": "publishedAt",
        "language": "en",
    }
    
    response = requests.get(NEWS_API_URL, params=params)
    response.raise_for_status()
    data = response.json()
    articles = data.get("articles", [])
    return articles
