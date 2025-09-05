import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-08-05&sortBy=publishedAt&apiKey=a9904621ac254fd2a5feac10dcf0a760"

try:
    r = requests.get(url)
    r.raise_for_status()  # Raises an HTTPError for bad responses
    news = r.json()  # Use .json() instead of json.loads(r.text)

    # Print the full response to see what we're getting
    print("API Response status:", news.get('status'))
    print("Total results:", news.get('totalResults'))

    # Check if the response contains articles
    if 'articles' in news and news['articles']:
        print(f"\nFound {len(news['articles'])} articles:\n")
        for article in news['articles']:
            print(f"Title: {article.get('title', 'No title')}")
            print(f"Description: {article.get('description', 'No description')}")
            print(f"URL: {article.get('url', 'No URL')}")
            print("--------------------------------------")
    else:
        print("No articles found or invalid response")
        if 'message' in news:
            print(f"Error message: {news['message']}")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
except json.JSONDecodeError as e:
    print(f"Failed to parse JSON response: {e}")
except KeyError as e:
    print(f"Missing expected key in response: {e}")
    print("Full response:", news)