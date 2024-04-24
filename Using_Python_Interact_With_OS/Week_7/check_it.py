import re
from collections import defaultdict
from collections import Counter
from itertools import groupby
from prettytable import PrettyTable
from config import Path, N_Path

def filter_error():
    try:
        with open(Path, "r+", encoding="utf-8") as file:
            re_data_search = r"ERROR\s(.*)\s\("
            text = file.read()
            results = re.findall(re_data_search, text)
            results.sort()

            group_results = [(key, len(list(group))) for key, group in groupby(results)]
            table = PrettyTable(["Error", "Count"])

            for result, count in group_results:
                table.add_row([result, count])
                table.sortby = "Count"
            print(table)

    except FileNotFoundError:
        print("None")

def filter_user():
    try:
        with open(Path, "r+", encoding="utf-8") as file:
            re_general = r"(INFO|ERROR)\s.*?\((.*?)\)"
            text = file.read()
            results_general = re.findall(re_general, text)
            results_general.sort()

            table = PrettyTable(["USER", "ERROR", "INFO"])
            single_results_general = Counter(results_general)  
            
            with open(N_Path, "w+", encoding="utf-8") as file:
                for key,value in single_results_general.items():
                    user_type, user_name = key
                    temp_listik = user_name,user_type,value
                    # file.write(f"{str(temp_listik)}\n")
                    file.write(", ".join(map(str, temp_listik)) + "\n")

            with open(N_Path, "r+", encoding="utf-8") as file:
                x = file.read().strip()
                result = x.split(', ')
                print(result)

               
    except FileNotFoundError:
        print("None")

if __name__=="__main__":
    filter_error()
    filter_user()