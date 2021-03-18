'''
Central Module
'''

from ReadingFiles import User_Input
from Converstion import RecieveList
import Decryption as de

''' 
Simple menu for test
'''
def Encrypt():

    ContentsOFile = []
    ContentsOFile = User_Input() 
    RecieveList(ContentsOFile)

def Decrypt(): 
    
    ContentsOFile = []
    ContentsOFile = User_Input() 
    de.RecieveList(ContentsOFile)