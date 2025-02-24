
from pydantic import BaseModel

class BlogPost(BaseModel):
    title: str
    content: str
    author: str
    published_at: str
    article_url: str
