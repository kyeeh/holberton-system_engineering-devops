#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""
from requests import get


def number_of_subscribers(subreddit):
    """
    Suscribers by subreddit
    """
    headers = {"user-agent": "kyeeh"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    try:
        req_data = get(url, headers=headers).json()
        subscriber_count = req_data["data"]["subscribers"]
        return (subscriber_count)
    except Exception:
        return 0
