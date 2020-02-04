#!/usr/bin/python3
"""script to export data in the CSV format"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    """script to export data in the CSV format"""
    url = "https://jsonplaceholder.typicode.com/"
    nameFile = ""
    responseUser = requests.get(url + 'users/' + argv[1]).json()
    responseTask = requests.get(url + 'todos?userId=' + argv[1]).json()

    nameFile = argv[1] + ".csv"
    myFile = open(nameFile, 'w')
    with myFile:
        obj = csv.writer(myFile, quoting=csv.QUOTE_ALL)
        for element in responseTask:
            obj.writerow([responseUser['id'], responseUser['username'],
                            element['completed'], element['title']])
