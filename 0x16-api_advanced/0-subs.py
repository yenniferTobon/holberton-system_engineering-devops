#!/usr/bin/python3
"""returns the number of subscribers"""
import requests
import json


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url)
    l = response.json()

    try:
        for key, value in l.items():
            if key == "data":
                print("yenn")
                for i, j in value.items():
                    if i == 'subscribers':
                        return (j)
    except:
        return(0)
