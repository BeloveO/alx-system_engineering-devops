#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts
    """
    url = "https://www.reddit.com/dev/api/{subreddit}/about.json".format(
                                                   subreddit=subreddit)
    user_agent = {'User-Agent': 'Python/requests'}
    payload = {'limit': '10'}
    res = requests.get(url, headers=user_agent,
                       params=payload, allow_redirects=False)
    if res.status_code in [302, 404]:
        print('None')
    else:
        res_json = res.json()
        if res_json.get('data') and res_json.get('data').get('children'):
            hotpost = res_json.get('data').get('children')
            for post in hotpost:
                if post.get('data') and post.get('data').get('title'):
                    print(post.get('data').get('title'))
