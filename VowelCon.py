
'''
Bro just run this once and check its out put
'''

def conversion(string):
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
    
    TransTable = string.maketrans(Key)
    
    return string.translate(TransTable)

def RecieveList(contents):
    print("Recieved contents: ", contents)
    convo = []
    for string in contents:
        convo.append(conversion(string))
    print (convo)

