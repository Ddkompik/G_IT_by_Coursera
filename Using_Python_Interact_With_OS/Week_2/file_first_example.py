from config import file_path

def FileCheck(file_path):
    '''Just using a method To Check The File Exist Or Nope.
        If Yes , Than Just Read the Context In File
        Using DOCSTRING To Describe The Process Without Comments'''
    try:
        with open(file_path, "x+", encoding="utf-8") as text:
            text.write("Hello")
            text.seek(0)
            text.read()

    except FileExistsError:
        with open(file_path, "r+", encoding="utf-8") as text:
            file = text.read()
            print(file)

if __name__ == "__main__":
    print(FileCheck.__doc__)
    FileCheck(file_path)
