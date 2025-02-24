import os
import openai
from dotenv import load_dotenv

load_dotenv(dotenv_path="config/.env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def generate_blog_post(article, prompt_config):
    # Load the prompt template from the configuration
    template = prompt_config.get("template", "")
    
    # Build the prompt by formatting the template with article details.
    prompt = template.format(
        title=article.get("title", ""),
        description=article.get("description", ""),
        content=article.get("content", "")
    )
    
    # Prepare messages for the Chat API
    messages = [
        {"role": "system", "content": "You are a helpful blog post writer."},
        {"role": "user", "content": prompt}
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=500  # Adjust tokens as needed
    )
    blog_post = response.choices[0].message.content.strip()
    return blog_post
