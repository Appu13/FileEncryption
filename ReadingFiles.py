'''
Module to read the file based on user input
convert it to a list and return the list
'''
def User_Input():
    # Get location from the user
    location = input("Enter the file location")
    contents_list =[]
    try:
        f = open(location,"r")
    except FileNotFoundError:
        print("Missing File")
        return

    # Read and store contents in a list    
    contents = f.read()
    contents_list = contents.split(",")
    
    f.close()
    return contents_list




