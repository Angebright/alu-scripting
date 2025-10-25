#!/usr/bin/python3
"""Fetches and prints top 10 hot post titles for a subreddit"""

import requests
import sys


def top_ten(subreddit):
    """Print titles of the top 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Python:subreddit.hot:v1.0 (by /u/yourusername)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get('data', {}).get('children', [])
        if not posts:
            print(None)
            return

        for post in posts:
            title = post.get('data', {}).get('title')
            if title is not None:
                print(title)
    except Exception:
        print(None)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        top_ten(sys.argv[1])
