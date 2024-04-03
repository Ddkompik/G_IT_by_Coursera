def FileCheck():
    '''Just using a method without Parameters To Check The File Exist Or Nope.
        If Yes , Than Just Read the Context In File
        Using DOCSTRING To Describe The Process Without Comments'''
    try:
        with open("C:\\Users\\dasha\\Documents\\CODE\\GitHub\\G_IT_by_Coursera\\Using_Python_Interact_With_OS\\Week_2\\example.txt", "x+") as text:
            text.write("Hello")
            text.read()
    except FileExistsError:
        with open("C:\\Users\\dasha\\Documents\\CODE\\GitHub\\G_IT_by_Coursera\\Using_Python_Interact_With_OS\\Week_2\\example.txt", "r+") as text:
            file = text.read()
            print(file)


if __name__ == "__main__":
    print(FileCheck.__doc__)
    FileCheck()
