import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

load_dotenv(dotenv_path="config/.env")

FIREBASE_CRED_PATH = os.getenv("FIREBASE_CRED_PATH")

# Initialize Firebase app if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_CRED_PATH)
    firebase_admin.initialize_app(cred)
    
db = firestore.client()

def post_blog(blog_post):
    # Create a new document in the "publications" collection
    doc_ref = db.collection("publications").document()
    doc_ref.set(blog_post)
    return doc_ref.id
