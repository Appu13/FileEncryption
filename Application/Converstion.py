
'''
Module to convert and store the recieved input
'''

from ReadingFiles import GetLocation

'''
 Used to:
  Recieve the contents of the read file 
  Call the conversion function
  Finally call the store method to store all the contents to the text 

'''
# Variables to measure the completion 
totalSize,currentSize = 0,0
convo = []



def RecieveList(contents):
    
    global totalSize
    global currentSize
    # Test if the recieved is empty
    if not contents:
        print("Missing")
        return
    
    
    totalSize = len(contents)
    currentSize = 0
    print("Encryption completion: ")
    
    
    for string in contents:
        convo.append(conversion(string))
        currentSize +=1
        print(currentSize/totalSize *100)
    
    Store()



# Method to convert the string based on a transtion table
def conversion(string):
   
   # key defintion for converstion
    Key = {
        'a': ';',
        'e': ':',
        'i': '*',
        'o': '@',
        'u': '$',
        'y': '|',
        'A': '[',
        'E': '!',
        'I': '^',
        'O': '~',
        'U': '&',
        'Y': '+'
    }
    
    # Making the transtion table
    TransTable = string.maketrans(Key)
    
    # Translating the string using the transition table
    return string.translate(TransTable)


# Used to store the contents into file name 
def Store():
    with open(GetLocation(), 'w') as filehandle:
        filehandle.truncate(0)
        filehandle.writelines(convo)
    print("Encryption is Done")

