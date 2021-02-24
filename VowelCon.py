
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
    
    key = string.maketrans(Key)
    print("Before Change: ",end="")
    print(string)
    print("After Change:" ,end="")
    print(string.translate(key))
conversion("Hi my name is Vishal. I am twenty years old. I like playing football")