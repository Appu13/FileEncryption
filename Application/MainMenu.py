from tkinter import Button,Tk
import tkinter.ttk as ttk

root=Tk()
root.title("Protect your Files")
root.geometry("400x400")
root.resizable(0,0)

#Encryption button function
def Encryption():
	pass

#Decryption button function
def Decryption():
	pass

#creating a main frame
#main_frame= Frame(root)
#main_frame.pack()

#Creation of Buttons
E_Button = Button(root,text="ENCRYPT",justify="center",width=20,command = Encryption)
D_Button = Button(root,text="DECRYPT",justify="center",width=20,command = Decryption)

#Arranging the buttons
E_Button.place(x=125,y=160)
D_Button.place(x=125,y=190)






root.mainloop()