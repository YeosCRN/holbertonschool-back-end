#!/usr/bin/python3
"""Exporting in JSON format"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    API_URL = 'https://jsonplaceholder.typicode.com'

    user_id = argv[1]
    response = requests.get(
        f'{API_URL}/users/{user_id}/todos',
        params={'_expand': 'user'}
    )

    if response.status_code == 200:
        data = response.json()
        dictionary = {user_id: []}

        with open(f'{user_id}.json', 'w',
                  encoding='utf-8') as file:
            for task in data:
                actual_dr = {
                    'task': task['title'],
                    'completed': task['completed'],
                    'username': task['user']['username']
                }
                dictionary[user_id].append(actual_dr)
            json.dump(dictionary, file)
    else:
        print(f'Error: {response.status_code}')
