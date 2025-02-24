from dotenv import load_dotenv
import os

# Load environment variables from the config/.env file
def load_config():
    load_dotenv(dotenv_path="config/.env")
    return {
        "news_api_key": os.getenv("NEWS_API_KEY"),
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
        "firebase_cred_path": os.getenv("FIREBASE_CRED_PATH")
    }

# You can add more shared dependencies (e.g., database sessions) here.
