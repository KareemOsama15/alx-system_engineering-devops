#!/usr/bin/python3
"""
script that, using this REST API, for all employees,
returns information about his/her TODO list progress in the JSON format..
"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    users_response = requests.get('{}users'.format(url))
    emp_json = users_response.json()

    emp_dict = {}
    for user in emp_json:
        username = user.get("username")
        userid = user.get("id")

        todos_response = requests.get('{}/todos?userId={}'.format(url, userid))
        todos_json = todos_response.json()
        emp_list = []
        for task in todos_json:
            tasks = {"username": username,
                     "task": task.get("title"),
                     "completed": task.get("completed")}
            emp_list.append(tasks)

        emp_dict[str(userid)] = emp_list

    with open("todo_all_employees.json", "w") as f:
        json.dump(emp_dict, f)
