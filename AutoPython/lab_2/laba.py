#!/usr/bin/env python3
import os
import requests

def addeed_feedback(dir, dict_def, result):
    for file_count in os.listdir(dir):
        if file_count.endswith(".txt"):
            f_line = f"{dir}{file_count}"
            with open(f_line, "r+", encoding="utf-8") as file:
                x = file.read().splitlines()
                result.append(dict(zip(dict_def, x)))

    for item in result:
        response = requests.post("http://IP_ADDRESS/feedback/", json=item)
        # print(response.request.body)
        # print(response.raise_for_status())
        if response.status_code !=201:
            raise Exception("ERROR STATUS ={}".format(response.status_code))

if __name__ == "__main__":
    result = []
    dir = "/data/feedback/"
    dict_def = ["title", "name", "date","feedback"]
    addeed_feedback(dir, dict_def, result)
