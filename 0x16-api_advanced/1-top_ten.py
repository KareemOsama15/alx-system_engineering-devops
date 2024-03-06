#!/usr/bin/python3
"""Module of function top_ten"""
import requests


def top_ten(subreddit):
    """
    function queries the Reddit API and prints
    the titles of the first 10 hot posts"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "user-agent"
    }
    # params = {
    #     'limit': 10
    # }
    response = requests.get(url,
                            headers=headers, 
                            # params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data['data']['children']
    for post in posts:
        print(post['data']['title'])
