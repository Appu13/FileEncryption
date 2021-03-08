'''
This is used to convert the string into a matrix

'''

# Declaring the variables
order = {}

# Method to splie as per the length
def split_len(seq,length):
    return[seq[i:i + length] for i in range (0, len(seq), length)]

# Create dictionary to store the keys
def encode(key, plaintext):
    order = {
        int (val): num for num, val in enumerate(key)
    }

# Getting input and key
plaintext = input("Enter the string")
key ='3241'

# Seting up the matrix
encode(key,plaintext)
ciphertext = ''

# Encoding the word
for index in sorted(order.keys()):
    for part in split_len(plaintext, len(key)):
        try: ciphertext += part[order[index]]
        except IndexError:
            continue



print(ciphertext)
