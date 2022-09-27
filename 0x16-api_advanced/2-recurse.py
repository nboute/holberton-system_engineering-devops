#!/usr/bin/python3
"""Get all hot posts from a subreddit using reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=None, session=None):
    """Get all hot posts from a subreddit"""
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json?t=all'
    if after is not None:
        url += '&after=' + after
    if (session is None):
        session = requests.Session()
        headers = {
            'User-Agent': 'My User Agent 1.0'
        }
        session.headers.update(headers)
    response = session.get(url, allow_redirects=False)
    if (response.ok is False):
        return None
    after = response.json().get('data').get('after')
    top_posts = response.json().get('data').get('children')
    for post in top_posts:
        hot_list.append(post.get('data').get('title'))
    if (after is None):
        return hot_list
    return recurse(subreddit, hot_list, after, session)
