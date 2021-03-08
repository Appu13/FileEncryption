location = ""

def User_Input():
    # Get location from the user
    global location
    location = input("Enter the file location")
    
    contents_list =[]
    try:
        with open(location,'r') as f:
            contents = f.read()
    except FileNotFoundError:
        print("Missing File")
        return

    contents_list = contents.split(",")
    
    return contents_list
