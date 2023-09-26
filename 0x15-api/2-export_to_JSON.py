#!/usr/bin/python3
"""
script uses REST API to return info about TODO list progress of an employee
"""
import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    userid = sys.argv[1]
    user = '{}users/{}'.format(url, userid)
    res = requests.get(user)
    json_o = res.json()
    name = json_o.get('username')

    todos = '{}todos?userId={}'.format(url, userid)
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        tdict = {"task": task.get('title'),
                 "completed": task.get('completed'),
                 "username": name}
        l_task.append(tdict)

    d_task = {str(userid): l_task}
    file = '{}.json'.format(userid)
    with open(file, mode='w') as f:
        json.dump(d_task, f)
