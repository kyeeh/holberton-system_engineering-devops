#!/usr/bin/python3
# using this REST API, for a given employee ID,
# returns information about his/her TODO list progress
# to export data in the CSV format.
import csv
from requests import get
from sys import argv


def api_to_csv(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    user = get(url + "users/{}".format(user_id)).json()
    tasks = get(url + "todos?userId={}".format(user_id)).json()
    with open("{}.csv".format(user_id), 'w', newline='') as csvfile:
        file_stream = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            file_stream.writerow([user_id, user.get("username"),
                                  task.get("completed"),
                                  task.get("title")])

if __name__ == "__main__":
    api_to_csv(int(argv[1]))
