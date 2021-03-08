'''
Central Module
'''

from ReadingFiles import User_Input
from Converstion import RecieveList
import Decryption as de

''' 
Simple menu for test
'''
option = int(input("Enter your choice: "))
ContentsOFile = []
ContentsOFile = User_Input()
if option == 1:
   
    RecieveList(ContentsOFile)
else: 
    
    de.RecieveList(ContentsOFile)