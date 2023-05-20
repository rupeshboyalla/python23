from tkinter import *
import webbrowser
from tkinter import Entry

root = Tk()
root.title("search bar")


def search(self):
    url = Entry.get()
    webbrowser.open(url)


label1= Label(root, text="enter search ", font=("stright", 30, "bold"))
label1.grid(row=0, column = 0)
entry = Entry(root, width=30)
entry.grid(row=0, column=1)
button = Button(root, text="search", command=search)
button.grid(row=1, column=0, columnspan=2, pady=10)
