from prompt import summarize_article_and_image
from extractor import extract_text_and_image


if __name__ == "__main__":
        
    url = 'https://www.bbc.com/news/world-europe-63863088'
    print("Extracting Data...")
    text, image_url = extract_text_and_image(url)

    print("Article Text Summary:", text[:500])  # Display the first 500 characters
    print("Image URL:", image_url)

    print(50*"*")


    summary = summarize_article_and_image(text, image_url)

    print("The summary from the openai is:\n", summary)
    




