#!/usr/bin/python3
"""Module of recurse function"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    headers = {
        "User-Agent": "user-agent"
    }
    response = requests.get(url,
                            headers=headers, 
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    for article in data['data']['children']:
        hot_list.append(article['data']['title'])

    if not data['data']['after']:
        return hot_list

    return recurse(subreddit, hot_list, data['data']['after'])
