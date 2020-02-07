#!/usr/bin/python3
"""returns the number of subscribers"""
import requests
import json


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    headers = {
        'User-Agent': 'My User Agent 1.0'
    }
    
    response = requests.get(url)
    l = response.json()

    try:
        return (l.get('data').get('subscribers'))
    except:
        return(0)
