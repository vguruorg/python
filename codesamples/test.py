from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar

root = Tk()
root.geometry("400x300")
root.title("Tutorial")

def clicked():
    messagebox.askyesno('This is a WARNING!', 'Do you wish to CONTINUE?')

label = Label(root, text = "Hello", font = ("Courier", 20))
button = Button(root, text = "Click Here", bg = "red", fg = "black", height = 50, width = 50, command = clicked)
bar = Progressbar(root, length=200)
bar["value"] = 25

label.place(x = 0, y = 0)
button.place(x = 0, y = 100)
bar.place(x = 0, y = 50)
root.mainloop()