import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import font

#frame section 
root = tkinter.Tk()
root.geometry("400x400")
root.resizable(6,6)
root.title("Simple_calculator")

#global variables


operators = ""
val = ""
A = 0
def key_1_ispressed():

    global val
    val = val + "1"
    data.set(val)

def key_2_ispressed():

    global val
    val = val + "2"
    data.set(val)

def key_3_ispressed():

    global val
    val = val + "3"
    data.set(val)

def key_4_ispressed():

    global val
    val = val + "4"
    data.set(val)

def key_5_ispressed():

    global val
    val = val + "5"
    data.set(val)

def key_6_ispressed():

    global val
    val = val + "6"
    data.set(val)


def key_7_ispressed():

    global val
    val = val + "7"
    data.set(val)

def key_8_ispressed():

    global val
    val = val + "8"
    data.set(val)

def key_9_ispressed():

    global val
    val = val + "9"
    data.set(val)


def key_0_ispressed():

    global val
    val = val + "0"
    data.set(val)

def key_pls_ispressed():

    global A
    global operator,val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def key_min_ispressed():

    global A
    global operator,val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def key_multiply_ispressed():

    global A
    global operator,val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def key_dvd_ispressed():

    global A
    global operator,val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def key_c_ispressed():

    global A
    global operator,val
    operator = ""
    val = ""
    A = 0
    data.set(val)

#result section
def result():
    global A,operator,val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        c = A + x
        val = str(c)
        data.set(val)
    if operator == "-":
        x = int((val2.split("-")[1]))
        c = A - x
        val = str(c)
        data.set(val)
    if operator == "*":
        x = int((val2.split("*")[1]))
        c = A * x
        val = str(c)
        data.set(val)
    if operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "Division By 0 Not Supported")
            A = ""
            val = ""
            data.set(val)
        else:
            C = int(A / x)
            data.set(C)

#lable section

data = StringVar()
lbl = Label(
    root,
    textvariable = data,
    font = ("verdana",23),
    anchor = SE,
    text = "label",
    background = "#000000",
    fg = "#ffffff"
)
lbl.pack(expand = True, fill = "both")

#button frame section
button1 = Frame(root)
button1.pack(expand = True, fill = "both")

button2 = Frame(root)
button2.pack(expand = True, fill = "both")

button3 = Frame(root)
button3.pack(expand = True, fill = "both")

button4 = Frame(root)
button4.pack(expand = True, fill = "both")

#button section
#raw1 
btn1 = Button(
    button1,
    text = "1",
    font = ("verdana",23),
    relief = GROOVE, border = 0,
    command = key_1_ispressed,
)
btn1.pack(side = LEFT,expand = True,fill = "both",)

btn2 = Button(
    button1,
    text = "2",
    font = ("verdana",23),
    relief = GROOVE, border = 0,
    command = key_2_ispressed,
)
btn2.pack(side = LEFT,expand = True,fill = "both",)

btn3 = Button(
    button1,
    text = "3",
    font = ("verdana",23),
    relief = GROOVE, border = 0,
    command = key_3_ispressed,
)
btn3.pack(side = LEFT,expand = True,fill = "both",)

btnpls = Button(
    button1,
    text = "+",
    font = ("verdana",23),
    relief = GROOVE, border = 0,
    command = key_pls_ispressed,
)
btnpls.pack(side = LEFT,expand = True,fill = "both",)

#raw2nd
btn4 = Button(
    button2,
    text = "4",
    font = ("verdana",23),
    relief = GROOVE, border = 0,
    command = key_4_ispressed,
)
btn4.pack(side = LEFT,expand = True,fill = "both",)

btn5 = Button(
    button2,
    text = "5",
    font = ("verdana",23),
    relief = GROOVE, border = 0,
    command = key_5_ispressed,
)
btn5.pack(side = LEFT,expand = True,fill = "both",)

btn6 = Button(
    button2,
    text = "6",
    font = ("verdana",23),
    relief = GROOVE, border = 0,
    command = key_6_ispressed,
)
btn6.pack(side = LEFT,expand = True,fill = "both",)

btnmin = Button(
    button2,
    text = "-",
    font = ("verdana",23),
    relief = GROOVE, border = 0,
    command = key_min_ispressed,
)
btnmin.pack(side = LEFT,expand = True,fill = "both",)

#raw3

btn7 = Button(
    button3,
    text = "7",
    font = ("verdana",23),
    relief = GROOVE, border = 0,
    command = key_7_ispressed,
)
btn7.pack(side = LEFT,expand = True,fill = "both",)

btn8 = Button(
    button3,
    text = "8",
    font = ("verdana",23),
    relief = GROOVE, border = 0,
    command = key_8_ispressed,
)
btn8.pack(side = LEFT,expand = True,fill = "both",)

btn9 = Button(
    button3,
    text = "9",
    font = ("verdana",23),
    relief = GROOVE, border = 0,
    command = key_9_ispressed,
)
btn9.pack(side = LEFT,expand = True,fill = "both",)

btnmultiply = Button(
    button3,
    text = "x",
    font = ("verdana",23),
    relief = GROOVE, border = 0,
    command = key_multiply_ispressed,
)
btnmultiply.pack(side = LEFT,expand = True,fill = "both",)

#raw4
btnc = Button(
    button4,
    text = "C",
    font = ("verdana",23),
    relief = GROOVE, border = 0,
    command = key_c_ispressed,
)
btnc.pack(side = LEFT,expand = True,fill = "both",)

btn0 = Button(
    button4,
    text = "0",
    font = ("verdana",23),
    relief = GROOVE, border = 0,
    command = key_0_ispressed,
)
btn0.pack(side = LEFT,expand = True,fill = "both",)

btnequal = Button(
    button4,
    text = "=",
    font = ("verdana",23),
    relief = GROOVE, border = 0,
    command = result,
)
btnequal.pack(side = LEFT,expand = True,fill = "both",)

btndvd = Button(
    button4,
    text = "/",
    font = ("verdana",23),
    relief = GROOVE, border = 0,
    command = key_dvd_ispressed,
)
btndvd.pack(side = LEFT,expand = True,fill = "both",)

root.mainloop()

