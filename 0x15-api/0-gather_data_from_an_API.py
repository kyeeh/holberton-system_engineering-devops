#!/usr/bin/python3
# using this REST API, for a given employee ID,
# returns information about his/her TODO list progress.
from sys import argv
from requests import get


if __name__ == "__main__":
    done = []
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users'
    user = get(url + "/{}".format(user_id)).json()
    tasks = get(url + "/{}/todos".format(user_id)).json()
    for task in tasks:
        if task.get("completed") is True:
            done.append(task.get("title"))
    print('Employee {} is done with tasks({}/{}):'
          .format(user.get('name'), len(done), len(tasks)))
    for task in done:
        print('\t {}'.format(task))
