#!/usr/bin/python3
"""Return to-do list for a given employee ID in CSV format"""
import requests
import sys
import pandas as pd

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(
        api_url + "todos", params={"userId": sys.argv[1]}).json()

    tasks_df = pd.DataFrame(
        todos, columns=["userId", "id", "title", "completed"])

    user_df = pd.DataFrame(data=[user], columns=[
                           "id", "name", "username", "email", "address", "phone", "website", "company"])

    merged_df = pd.merge(tasks_df, user_df, on="id", how="outer")[
        ["id", "username", "completed", "title"]]

    filename = str(user.get("git")) + ".csv"
    merged_df.to_csv(filename, index=False)
