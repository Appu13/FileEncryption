'''
Module to read the file based on user input
convert it to a list and return the list
'''
def User_Input():
    # Get location from the user
    location = input("Enter the file location")
    contents_list =[]
    try:
       with open (location, 'r') as f:
           contents = f.read()
    except FileNotFoundError:
        print("Missing File")
        return

    # Store contents as a list
    contents_list = contents.split(",")

    return contents_list




