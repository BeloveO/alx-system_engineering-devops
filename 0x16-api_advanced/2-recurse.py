#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    returns list of all hot titles of a subreddit
    """
    url = "https://www.reddit.com/dev/api/{subreddit}/about.json".format(
                                                   subreddit=subreddit)
    user_agent = {'User-Agent': 'Python/requests'}
    payload = {'after': '', 'limit': '100'}
    res = requests.get(url, headers=user_agent,
                       params=payload, allow_redirects=False)
    if res.status_code == 200:
        res = res.json
        hotposts = res.get('data').get('children')
        after = res.get('data').get('after')
        for post in hotposts:
            hot_list.append(post.get('data').get('title'))
        if subreddit is not None:
            recurse(subreddit, hot_list=[])
        return hot_list
    return None
