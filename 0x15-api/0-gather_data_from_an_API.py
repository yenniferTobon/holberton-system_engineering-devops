#!/usr/bin/python3
""" requests to an api with REST API"""

from sys import argv
import requests


if __name__ == "__main__":
    """funtion to requests to an api"""
    url = "https://jsonplaceholder.typicode.com/"
    responseUser = (requests.get(url + 'users/' + argv[1]).json()).get('name')
    responseTask = len(requests.get(url + 'todos?userId=' + argv[1]).json())
    responseTaskDone = requests.get(url + "todos?userId={}&&completed=true".
                                    format(argv[1])).json()

    print("Employee {} is done with tasks({}/{}):".
          format(responseUser, len(responseTaskDone), responseTask))

    for element in responseTaskDone:
        print("\t ", element.get('title'))
