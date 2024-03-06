#!/usr/bin/python3
"""Module of number_of_subscribers function"""
import requests


def number_of_subscribers(subreddit):
    """
    function queries the Reddit API
    and returns the number of subscribers"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'user-agent'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json()
    subscribers = data['data']['subscribers']

    return subscribers
