#!/usr/bin/python3
"""This module scraps REST API from a placeholder website"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        exit()
    response = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(argv[1])).json()
    print("Employee {} is done with tasks"
          .format(response.get('name')), end='')
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1])
    response = requests.get(url).json()
    task_list = []
    nb_tasks = len(response)
    nb_tasks_completed = 0
    for task in response:
        if task.get('completed') is True:
            nb_tasks_completed += 1
            task_list.append(task.get('title'))
    print('({}/{}):'.format(nb_tasks_completed, nb_tasks))
    for task in task_list:
        print("\t " + task)
