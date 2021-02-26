'''
Created on 15-Feb-2021

Read the file and then pass the list to the next function

@author: Appu13
'''

from os import path



def User_Input():
    location = input("Enter the file location")
    contents_list =[]
    try:
        f = open(location,"r")
    except FileNotFoundError:
        print("Missing File")
        return
    contents = f.read()
    contents_list = contents.split(",")
    
    f.close()
    return contents_list


User_Input()


