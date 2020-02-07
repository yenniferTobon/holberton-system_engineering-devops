#!/usr/bin/python3
"""prints the titles of the first 10 hot posts"""
import requests
import json


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    url = 'https://api.reddit.com/r/{}?sort=hot&limit=10'.format(subreddit)

    response = requests.get(url)
    l = response.json()

    headers = {
        'User-Agent': "My User Agent 1.0"
    }

    if response.status_code == 200:
        result = l.get('data').get('children')

        for child in result:
            title = child.get("data").get("title")
            print(title)
    else:
        print(None)
