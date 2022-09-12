#!/usr/bin/python3
"""This module scraps REST API from a website and exports it to json"""
import requests
import json


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users/").json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = tasks.json()
    my_dict = {}
    users_dict = {}
    for user in users:
        users_dict[user.get('id')] = user.get('username')

    for task in tasks:
        userId = task.get('userId')
        task['username'] = users_dict.get(userId)
        task['task'] = task['title']
        task['completed'] = task.pop('completed')
        task.pop('title')
        task.pop('id')
        task.pop('userId')
        if my_dict.get(userId) is None:
            my_dict[userId] = []
        my_dict[userId].append(task)

    with open("todo_all_employees.json", "w") as f:
        f.write(json.dumps(my_dict))
