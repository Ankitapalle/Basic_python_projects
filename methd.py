import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import font
from typing import Text

#frame section 
root = tkinter.Tk()
root.geometry("400x400")
root.resizable(6,6)
root.title("String Methods")

def Capitalize():

    #capitalize()

    strg = "welcome to the code of method :)"
    print("strg = welcome to the code of method :)")
    print("print(strg.capitalize())")
    print(strg.capitalize())
def centerStr():

    #center(width)

    str1 = "Hello Welcome!"

    n_string = str1.center(50) 
    #as you will increase or decrease "width" you see the diffrence in space

    print("A new string is",n_string)

#string frame section

btn1 = Frame(root)
btn1.pack(expand = True, fill = "both")

center = Frame(root)
center.pack(expand = True, fill = "both")

#raw1 
capital = Button(
        btn1,
    text = "capitalization()",
    font = ("verdana",23),
    relief = SUNKEN, border = 0,
    command = Capitalize(),
)
capital.pack(side = LEFT,expand = True,fill = "both",)

centerString = Button(
    btn1,
    text = "center(width)",
    font = ("verdana",23),
    relief = SUNKEN, border = 0,
    command = centerStr(),
)
centerString.pack(side = LEFT,expand = True,fill = "both",)

root.mainloop()
