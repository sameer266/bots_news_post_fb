import requests
import facebook as fb
import os
import json

# Configuration
news_api_key = os.getenv("NEWS_API_KEY")
facebook_access_token = os.getenv("FACEBOOK_ACCESS_TOKEN")
news_api_url = f"https://newsdata.io/api/1/news?apikey={news_api_key}&q=Nepal&country=np&language=en,ne&category=business,crime,education,politics,tourism"
graph = fb.GraphAPI(facebook_access_token)
posted_urls_file = 'posted_urls.json'

# Load posted URLs from file
if os.path.exists(posted_urls_file):
    with open(posted_urls_file, 'r') as f:
        posted_urls = set(json.load(f))
else:
    posted_urls = set()

def fetch_latest_news():
    response = requests.get(news_api_url)
    if response.status_code == 200:
        articles = response.json().get('results')
        if articles:
            # Find an article with an image that hasn't been posted yet
            for article in articles:
                if article.get('image_url') and article.get('link') not in posted_urls:
                    return article
    return None

def download_image(image_url):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        return response.content
    return None

def post_news_with_image_to_facebook():
    news_article = fetch_latest_news()
    if news_article:
        # Print the news article for debugging
        print(news_article)
        
        title = news_article['title']
        url = news_article['link']
        image_url = news_article.get('image_url')
        
        message = f"{title}\nRead more: {url}"
        
        if image_url:
            image_data = download_image(image_url)
            if image_data:
                try:
                    graph.put_photo(image=image_data, message=message)
                    print("Successfully posted the latest news with image to Facebook")
                    posted_urls.add(url)  # Add the URL to the set of posted URLs

                    # Save posted URLs to file
                    with open(posted_urls_file, 'w') as f:
                        json.dump(list(posted_urls), f)
                        
                except fb.GraphAPIError as e:
                    print(f"An error occurred: {e}")
            else:
                print("Failed to download the image")
        else:
            print("No image found for the article")
    else:
        print("No news articles found")

if __name__ == "__main__":
    post_news_with_image_to_facebook()
    
