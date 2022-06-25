'''Importing libraries'''
from tkinter import *
import random, string
import pyperclip          # It is use to copy and paste text to and from the clipboard to your computer


'''Initializing Window'''
root = Tk()
root.geometry('600x600')
root.resizable(0,0)                #(0,0)---> sets the fix size of the window
root.title("Password Generator")
Label(root, text= "Password Generator", font= 'arial 20 bold').pack()
Label(root, text= "By VKP", font= "arial 10 italic").pack(side= BOTTOM)


''' Select password length '''
pass_label = Label(root, text= "Password Length", font= 'arial 10 bold').pack()
pass_len = IntVar()      #It is an integer type variable that stores the length of a password
length = Spinbox(root, from_ = 8, to_ = 32, textvariable = pass_len, width= 15).pack()    
#Spinbox is used to to select the password length it is used from fixed number of values (here it is 8 - 32)


'''Function to generate Password'''
pass_str = StringVar()
def Generator():
    password = ''
    
    for x in range(0,4):
        Password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
        
    for y in range(pass_len.get()-4):
        Password = Password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(Password)


'''Defining buttons'''
Button(root, text= "Generate Password", command= Generator).pack(pady= 5)
Entry(root, textvariable= pass_str).pack()


'''Function to copy password'''
def copypass():
    pyperclip.copy(pass_str.get())
    
Button(root, text= "Click to Copy", command= copypass).pack(pady= 5)


'''Run the code and GUI'''
root.mainloop()