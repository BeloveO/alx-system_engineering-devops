#!/usr/bin/python3
"""
script uses REST API to return info about TODO list progress of an employee
"""
import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    res = requests.get(user)
    json_o = res.json()
    d_task = {}
    for user in json_o:
        name = json_o.get('username')
        userid = user.get('id')
        todos = '{}todos?userId={}'.format(url, userid)
        res = requests.get(todos)
        tasks = res.json()
        l_task = []
        for task in tasks:
            tdict = {"username": name,
                     "task": task.get('title'),
                     "completed": task.get('completed')}
            l_task.append(tdict)

        d_task[str(userid)] = l_task
    file = 'todo_all_employees.json'
    with open(file, mode='w') as f:
        json.dump(d_task, f)
