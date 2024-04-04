from config import file_path
import re

def find_it(file_path, data):
    '''DOCSTRING: Find a String That need a User'''
    try:
        with open(file_path, "r+", encoding="utf-8") as file:
            text = file.read()
            if data in text:
                print(text.index(data), data)
            else:
                print("Data Not Found")

        with open(file_path, "r+", encoding="utf-8") as file:
            re_file = file.read()
            find_q = r"\d{4}"
            match_data = re.findall(find_q, re_file)
            print(match_data)
 
    except FileNotFoundError:
        print("File Error. Check It")

if __name__ == "__main__":
    # data = input("PLease add the word that you want to find it: ")
    data = "Fin"
    find_it(file_path, data)