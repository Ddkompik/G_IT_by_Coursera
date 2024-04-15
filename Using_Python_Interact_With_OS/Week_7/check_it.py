from prettytable import PrettyTable
from itertools import groupby
from config import Path
import re

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

if __name__=="__main__":
    filter_error()