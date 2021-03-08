'''
Module to read the file based on user input
convert it to a list and return the list
'''

location = ""
def User_Input():
    global location
    location = input("Enter the file location")
    contents_list =[]
    try:
        with open(location,'r') as f:
            contents_list = f.readlines()
    except FileNotFoundError:
        print("Missing File")
        return

    return contents_list

def GetLocation():
    global location
    return location




