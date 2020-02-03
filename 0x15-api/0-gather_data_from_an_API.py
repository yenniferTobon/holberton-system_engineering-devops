#!/usr/bin/python3
""" REST API requests """

import requests
from sys import argv
import json


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    responseUser = requests.get(url + '/users/' + argv[1]).json()
    responseTask = len(requests.get(url + '/todos?userId=' + argv[1]).json())
    responseTaskDone = requests.get(url + "/todos?userId={}&&completed=true".
                                    format(argv[1])).json()

    print('Employee {} is done with tasks({}/{}): '.
          format(responseUser['name'], len(responseTaskDone), responseTask))

    for element in responseTaskDone:
        print("\t", element['title'])
