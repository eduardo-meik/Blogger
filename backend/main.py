from fastapi import FastAPI
from routers import blog

app = FastAPI()

# Include the blog router (all endpoints related to blog generation)
app.include_router(blog.router, prefix="/blog", tags=["Blog"])

@app.get("/")
def read_root():
    return {"message": "FastAPI Blog Generator is running"}
