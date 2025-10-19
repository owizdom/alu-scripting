#!/usr/bin/python3
"""
Reddit API Top Ten Hot Posts
"""
import requests
import sys


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.
    
    Args:
        subreddit (str): The subreddit to query
        
    Returns:
        None: Prints the titles or None if invalid subreddit
    """
    # Reddit API endpoint for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Headers to identify the script (required by Reddit API)
    headers = {
        'User-Agent': 'RedditTopTen/1.0 by owzidom'
    }
    
    try:
        # Make request without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response is a redirect (indicates invalid subreddit)
        if response.status_code in [301, 302, 303, 307, 308]:
            print("None")
            return
        
        # Check if request was successful
        if response.status_code != 200:
            print("None")
            return
            
        # Parse JSON response
        data = response.json()
        
        # Check if we have posts data
        if 'data' not in data or 'children' not in data['data']:
            print("None")
            return
            
        posts = data['data']['children']
        
        # Print titles of first 10 posts
        for i, post in enumerate(posts[:10]):
            if 'data' in post and 'title' in post['data']:
                print(post['data']['title'])
                
    except requests.exceptions.RequestException:
        print("None")
    except (KeyError, ValueError):
        print("None")
    except Exception:
        print("None")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
