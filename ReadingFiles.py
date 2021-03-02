'''
Module to read the file based on user input
convert it to a list and return the list
'''
def User_Input():
    # Get location from the user
    location = input("Enter the file location")
    contents_list =[]
    try:
        with open(location,'r') as f:
            contents_list = f.readlines()
    except FileNotFoundError:
        print("Missing File")
        return

    return contents_list

User_Input()




