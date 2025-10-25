#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests


def top_ten(subreddit):
    """Return number of subscribers if @subreddit is valid subreddit.
    if not return 0."""

    if not subreddit:
        print(None)
        return

    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(
        subreddit_url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        json_data = response.json()
        children = json_data.get('data', {}).get('children', [])[:10]
        for post in children:
            print(post.get('data', {}).get('title'))
    except (ValueError, KeyError):
        print(None)
