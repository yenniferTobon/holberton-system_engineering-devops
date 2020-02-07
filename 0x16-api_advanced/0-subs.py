#!/usr/bin/python3
"""returns the number of subscribers"""
import requests
import json


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url)
    l = response.json()

    print(response.headers.get('User-Agent'))
    headers = {
            'User-Agent': '"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"'
            }

    if response.status_code == 200:
        for key, value in l.items():
            if key == "data":
                for i, j in value.items():
                    if i == 'subscribers':
                        return (j)
    else:
        return(0)