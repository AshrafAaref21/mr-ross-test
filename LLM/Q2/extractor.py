import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
from urllib.parse import urljoin

# Function to extract text and image from a URL
def extract_text_and_image(url):
    # Send GET request to fetch HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract article text (specific tag/class should be adjusted based on the site structure)
    article_text = ' '.join([p.get_text() for p in soup.find_all('p')])

    # Find the first image in the article
    img_tag = soup.find('img')
    img_url = img_tag['src'] if img_tag else None

    # Ensure the image URL is absolute
    if img_url:
        img_url = urljoin(url, img_url)  # Create absolute URL
        # Fetch the image content
        img_response = requests.get(img_url)
        img = Image.open(BytesIO(img_response.content))

        # Print image details
        print(f"Image Format: {img.format}")
        print(f"Color Mode: {img.mode}")
        print(f"Dimensions: {img.size}")

    # Return the extracted text
    return article_text, img_url

# Example usage
url = 'https://www.bbc.com/news/world-europe-63863088'
text, image_url = extract_text_and_image(url)
print("Article Text Summary:", text[:500])  # Display the first 500 characters
print("Image URL:", image_url)
