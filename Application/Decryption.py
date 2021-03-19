'''
This module is used to decrypt the passed list

'''

from ReadingFiles import GetLocation



# Variables to measure the completion 
totalSize,currentSize = 0,0
convo = []

def RecieveList(contents):
    
    if not contents:
        print("Missing")
        return
    
       
    totalSize = len(contents)
    currentSize = 0
    print("Decryption completion: ")
    
    
    for string in contents:
        convo.append(conversion(string))
        currentSize +=1
        print(currentSize/totalSize *100)
    Store()


def conversion(string):
    Key = {
        ';': 'a',
        ':': 'e',
        '*': 'i',
        '@': 'o',
        '$': 'u',
        '|': 'y',
        '[': 'A',
        '!': 'E',
        '^': 'I',
        '~': 'O',
        '&': 'U',
        '+': 'Y'
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
    print("Decryption is Done")
