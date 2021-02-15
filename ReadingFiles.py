'''
Created on 15-Feb-2021

Read the file and then pass the list to the next function

@author: Appu13
'''

from os import path

location = input("Enter the file location ")

def CheckFile():
    
    if not path.exists(location):
        return False
    else:
        return True 


if CheckFile():
    print("Opened", location)
    # Create the function to code the file 
   
else:
    print("Missing", location)
    # Display the error message