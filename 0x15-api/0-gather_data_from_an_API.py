#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = sys.argv[1]

    users_response = requests.get('{}users?id={}'.format(url, emp_id))
    emp_json = users_response.json()
    print("Employee {} is done with tasks".format(emp_json.get("name")), end='')

    todos_response = requests.get('{}/todos?userId={}'.format(url, emp_id))
    todos_json = todos_response.json()

    success_tasks = []
    for task in todos_json:
        if task.get("completed") is True:
            success_tasks.append(task)
    print("({}/{}):".format(len(success_tasks), len(todos_json)))

    for task in success_tasks:
        print("\t {}".format(task.get('title')))
