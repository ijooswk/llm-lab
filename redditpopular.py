import requests
import os
from dotenv import load_dotenv
from email_service import EmailService

# Load environment variables
load_dotenv()

# Reddit API credentials
CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
NAVER_USER = os.getenv('NAVER_USER')
NAVER_PASSWORD = os.getenv('NAVER_PASSWORD')

USER_AGENT = 'MyBot/1.0'

# subreddits list
subreddits = [
    "generativeAI",
    "cloudcomputing",
    "MachineLearning",
    "opensource",
    "FlutterDev",
    "Kubernetes",
]

def get_reddit_auth_token():
    """Get Reddit API authentication token"""
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    headers = {'User-Agent': USER_AGENT}
    data = {
        'grant_type': 'client_credentials',
    }
    
    response = requests.post(
        'https://www.reddit.com/api/v1/access_token',
        auth=auth,
        data=data,
        headers=headers
    )
    return response.json()['access_token']

def get_popular_reddit_articles(subreddits):
    """Get today's popular articles from specified subreddits"""
    from datetime import datetime, timezone
    import time

    popular_articles = []
    token = get_reddit_auth_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'User-Agent': USER_AGENT
    }

    # Get today's timestamp (midnight UTC)
    today = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    today_timestamp = int(today.timestamp())

    for subreddit in subreddits:
        try:
            url = f"https://oauth.reddit.com/r/{subreddit}/new"  # Changed to /new for latest posts
            response = requests.get(
                url,
                headers=headers,
                params={
                    'limit': 10,  # Increased limit to find more today's posts
                    'sort': 'new',
                    'after': f"t3_{today_timestamp}"
                }
            )
            response.raise_for_status()
            
            data = response.json()
            for item in data['data']['children']:
                post_time = int(item['data']['created_utc'])
                
                # Only include posts from today
                if post_time >= today_timestamp:
                    title = item['data']['title']
                    selftext = item['data']['selftext']
                    link = f"https://reddit.com{item['data']['permalink']}"
                    score = item['data']['score']
                    num_comments = item['data']['num_comments']
                    
                    popular_articles.append({
                        'title': title,
                        'link': link,
                        'subreddit': subreddit,
                        'selftext': selftext,
                        'score': score,
                        'comments': num_comments,
                        'created_utc': post_time,
                        'posted': datetime.fromtimestamp(post_time, tz=timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
                    })
        except Exception as e:
            print(f"Error fetching from r/{subreddit}: {str(e)}")
            continue

    # Sort by score (popularity)
    popular_articles.sort(key=lambda x: x['score'], reverse=True)
    return popular_articles

# This script will get the summary from the transcript of a youtube video and call ollama API (local) to summarize it.
def summarize_transcript(transcript, model="gemma:7b"):
    # Combine transcript text
    article_texts = []
    for idx, article in enumerate(transcript, 1):
        article_text = f"Article {idx} from r/{article['subreddit']}:\n"
        article_text += f"Title: {article['title']}\n"
        article_text += f"Content: {article['selftext']}\n"
        article_texts.append(article_text)      
    
    full_text = "\n\n".join(article_texts)
    
    prompt = f"Please provide a summary of the key technology trends discussed in these articles.:\n\n{full_text}"
    print("Calling Ollama API...")
    # Call Ollama API
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )
    if response.status_code == 200:
        result = response.json()
        return result.get("response", "").strip()
    else:
        print(f"Ollama API error: {response.status_code} {response.text}")
        return None
def main():
    try:
        # Get the most popular 10 articles from Reddit
        articles = get_popular_reddit_articles(subreddits)

        summary = summarize_transcript(articles)
        # Initialize the email service (configure as needed)
        email_service = EmailService(NAVER_USER, NAVER_PASSWORD)

        # Compose email details
        subject = "Reddit Technology Trends Summary"
        body = summary
        recipients = "ijooswk@gmail.com"  # Replace with actual recipient(s)
        
        # Print the results
        raw_data = ""
        for idx, article in enumerate(articles, 1):
            raw_data += f"{idx}. [r/{article['subreddit']}] {article['title']}"
            raw_data += f"Link: {article['link']}\n"

        # Send the email
        email_service.send_email(recipients, subject, raw_data + body)

    except Exception as e:
        print(f"An error occurred: {str(e)}")



if __name__ == "__main__":
    main()