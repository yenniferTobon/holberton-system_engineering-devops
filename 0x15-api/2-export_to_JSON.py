#!/usr/bin/python3
""" script to export data in the JSON format"""

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    """script to export data in the JSON format"""
    url = "https://jsonplaceholder.typicode.com/"
    output = {}
    listTask = []
    responseUser = requests.get(url + 'users/' + argv[1]).json()
    responseTask = requests.get(url + 'todos?userId=' + argv[1]).json()

    for element in responseTask:
        listTask.append({'task': element['title'],
                         'completed': element['completed'],
                         'username': responseUser['username']})

    output = {argv[1]: listTask}

    nameFile = argv[1] + ".json"
    myFile = open(nameFile, 'w')
    with myFile:
        json.dump(output, myFile)
