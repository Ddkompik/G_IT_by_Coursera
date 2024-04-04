from config import csv_file_path
import json

def FileCheck(data):
    try:
        with open (csv_file_path, "x+") as path:
            data = json.dumps(data)
            path.write(data)

    except FileExistsError:
        with open(csv_file_path, "r+") as path:
            content = path.read()
            data = json.loads(content)
            print(data)


if __name__ == "__main__":
    list_data_num = list(x for x in range(1,11))
    FileCheck(list_data_num)
    