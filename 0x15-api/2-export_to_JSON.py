#!/usr/bin/python3
# using this REST API, for a given employee ID,
# returns information about his/her TODO list progress.
from sys import argv
from requests import get


if __name__ == "__main__":
    done = []
    url = "https://jsonplaceholder.typicode.com/users"
    user = get(url + "/{}".format(argv[1])).json()
    tasks = get(url + "/{}/todos".format(argv[1])).json()
    for task in tasks:
        if task["completed"]:
            done.append(task.get("title"))
    print('Employee {} is done with tasks({}/{}):'
          .format(user.get('name'), len(done), len(tasks)))
    for task in done:
        print('\t {}'.format(task))
