#!/usr/bin/python3
"""
script uses REST API to return info about TODO list progress of an employee
"""
import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/'.format(url)
    res = requests.get(user)
    json_o = res.json()
    with open("todo_all_employees.json", "w") as file:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in json_o}, file)
    