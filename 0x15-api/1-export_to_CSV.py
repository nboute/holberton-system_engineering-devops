#!/usr/bin/python3
"""This module scraps REST API from a website and exports it to csv"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        exit()
    response = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(argv[1])).json()
    username = response.get('username')
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1])
    response = requests.get(url).json()
    with open("{}.csv".format(argv[1]), "w") as f:
        for task in response:
            f.write('"{}","{}","{}","{}"\n'.format(argv[1],
                                                   username,
                                                   task.get('completed'),
                                                   task.get('title')))
