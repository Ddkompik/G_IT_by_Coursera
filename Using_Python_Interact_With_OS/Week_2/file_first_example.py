from config import file_path
import os
import getpass
import datetime

def FileCheck(file_path):
    '''Just using a method To Check The File Exist Or Nope.
        If Yes , Than Just Read the Context In File
        Using DOCSTRING To Describe The Process Without Comments'''
    try:
        with open(file_path, "x+", encoding="utf-8") as text:
            text.write(f"Hello {getpass.getuser()}")
            text.seek(0)
            content = text.read()
            print(content)

    except FileExistsError:
        with open(file_path, "r+", encoding="utf-8") as text:
            file = text.read()
            print(file)

if __name__ == "__main__":
    print(FileCheck.__doc__)
    FileCheck(file_path)

    file_path_time_conv = os.path.getmtime(file_path)
    file_path_date = datetime.datetime.fromtimestamp(file_path_time_conv)
    print("GENERAL INFO: Size:{0:.3f} KB, Date:{1}".format(os.path.getsize(file_path)/1024, file_path_date.strftime("%Y:%m:%d")))
    
