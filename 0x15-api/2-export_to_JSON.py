#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress in the JSON format..
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = sys.argv[1]

    users_response = requests.get('{}users?id={}'.format(url, emp_id))
    emp_json = users_response.json()
    emp_name = emp_json[0].get('username')

    todos_response = requests.get('{}/todos?userId={}'.format(url, emp_id))
    todos_json = todos_response.json()

    emp_list = []
    for task in todos_json:
        tasks = {}
        tasks["task"] = task.get("title")
        tasks["completed"] = task.get("completed")
        tasks["username"] = emp_name
        emp_list.append(tasks)

    emp_dict = {str(emp_id): emp_list}
    with open(f"{emp_id}.csv", "w") as f:
        json.dump(emp_dict, f)
