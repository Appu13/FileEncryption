
'''
Used to convert the contents of the file
'''

# Method to convert the string based on a transtion table
def conversion(string):
   
   # key defintion for converstion
    Key = {
        'a': ';0',
        'e': ':(',
        'i': '*',
        'o': '@#',
        'u': '$%',
        'y': '|`',
        'A': '[]',
        'E': '!@',
        'I': '^%',
        'O': '~|',
        'U': '&#@',
        'Y': '!$)*'
    }
    
    # Making the transtion table
    TransTable = string.maketrans(Key)
    
    # Translating the string using the transition table
    return string.translate(TransTable)


# Used to recieve the contents of the read file and call the conversion function 
def RecieveList(contents):

    print("Recieved contents: ", contents)
    convo = []
    
    for string in contents:
        convo.append(conversion(string))
    
    print ("Converted text: ",convo)

