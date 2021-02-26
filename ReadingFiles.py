'''
Created on 15-Feb-2021

Read the file and then pass the list to the next function
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




