#!/usr/bin/python3
"""script to export data in the JSON format."""

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    """script to export data in the JSON format."""
    url = "https://jsonplaceholder.typicode.com/"
    output = {}
    listTask = []
    nameFile = "todo_all_employees.json"
    responseUser = requests.get(url + 'users/').json()
    responseTask = requests.get(url + 'todos/').json()

    for User in responseUser:
        listTask = []
        for element in responseTask:
            listTask.append({'task': element['title'],
                             'completed': element['completed'],
                             'username': User['username']})
        output[User['id']] = listTask

    myFile = open("todo_all_employees.json", 'w')
    with myFile:
        json.dump(output, myFile)
