#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress in the CSV format.
"""
import csv
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

    user_list = []
    for task in todos_json:
        title = task.get('title')
        status = task.get('completed')
        user_list.append([emp_id, emp_name, status, title])

    with open(f"{emp_id}.csv", "w") as f:
        writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(user_list)
