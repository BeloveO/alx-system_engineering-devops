#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{subreddit}/about.json".format(
        subreddit=subreddit)
    user_agent = {'User-Agent': 'Python/requests'}
    res = requests.get(url, headers=user_agent, allow_redirects=False)
    if res.status_code in [302, 404]:
        return 0
    return res
