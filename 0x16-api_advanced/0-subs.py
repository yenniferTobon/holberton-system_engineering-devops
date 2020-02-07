#!/usr/bin/python3
"""returns the number of subscribers"""
import json
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    headers = {
        'User-Agent': 'My User Agent 1.0'
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    l = response.json()

    if response.status_code == 200:
        for key, value in l.items():
            if key == "data":
                for i, j in value.items():
                    if i == 'subscribers':
                        return (j)
    else:
        return(0)
