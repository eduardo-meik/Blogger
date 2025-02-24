import json
from fastapi import APIRouter, HTTPException
from models.blog_post import BlogPost
from services.news_service import fetch_news
from services.openai_service import generate_blog_post
from services.firebase_service import post_blog

router = APIRouter()

@router.post("/generate-blog")
def generate_blog():
    try:
        # Fetch news articles
        articles = fetch_news()
        if not articles:
            raise HTTPException(status_code=404, detail="No articles found")
        
        # Select the first article
        article = articles[0]

        # Load prompt configuration from config/prompt.json
        with open("config/prompt.json", "r") as f:
            prompt_config = json.load(f)

        # Generate blog post content via OpenAI
        blog_content = generate_blog_post(article, prompt_config)

        # Construct blog post object using Pydantic
        blog_post = BlogPost(
            title=article.get("title", "Untitled"),
            content=blog_content,
            author=article.get("author", "Unknown"),
            published_at=article.get("publishedAt", ""),
            article_url=article.get("url", "")
        )

        # Post blog post to Firebase Firestore
        blog_id = post_blog(blog_post.dict())

        return {"message": "Blog post generated successfully", "blog_id": blog_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
