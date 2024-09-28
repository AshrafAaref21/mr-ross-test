import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
)


def summarize_article_and_image(article_text, image_url):
    """
    Summarizes the article content and image using OpenAI's LLM.

    Parameters:
    - article_text: The text content of the article
    - image_url: The URL of the associated image

    Returns:
    - summary: The summary of the article and image
    """
    prompt = f"Summarize the following article content and its associated image:\n\n" \
             f"Article Text: {article_text}\n" \
             f"Image URL: {image_url}\n\n" \
             f"Provide a concise summary within 90 words."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Specify the model
        messages=[{"role": "user", "content": prompt}],
    )

    summary = response.choices[0].message.content.strip()
    return summary



