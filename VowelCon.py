
'''
Bro just run this once and check its out put

Weakness:
    it only replaces the vowels so if hackers spend some they can rebuild the key

Improvement:
    We find the common pairing of vowels and consonets and replace them
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