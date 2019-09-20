#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
from requests import get


def top_ten(subreddit):
    """
    The first 10 hot posts by subreddit
    """
    headers = {"user-agent": "kyeeh"}
    url = "https://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    try:
        req_data = get(url, headers=headers, allow_redirects=False).json()
        hot_posts = req_data["data"]["children"]
        for post in hot_posts:
            print(post['data']['title'])
    except Exception:
        print("None")
