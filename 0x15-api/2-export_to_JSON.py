#!/usr/bin/python3
"""This module scraps REST API from a website and exports it to json"""
import requests
from sys import argv
import json


if __name__ == "__main__":
    if len(argv) < 2:
        exit()
    response = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(argv[1])).json()
    username = response.get('username')
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1])
    response = requests.get(url).json()
    for task in response:
        task['task'] = task['title']
        task['completed'] = task.pop('completed')
        task['username'] = username
        task.pop('title')
        task.pop('id')
        task.pop('userId')

    dict = {argv[1]: response}

    with open("{}.json".format(argv[1]), "w") as f:
        f.write(json.dumps(dict))
