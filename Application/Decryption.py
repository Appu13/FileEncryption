'''
This module is used to decrypt the passed list

'''

from ReadingFiles import GetLocation
convo = []

def RecieveList(contents):
    
    if not contents:
        print("Missing")
        return
    
    for string in contents:
        convo.append(conversion(string))
    
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
    print("Done")
