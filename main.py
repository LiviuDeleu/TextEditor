# import statements
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import Font
from tkinter.scrolledtext import *
import file_menu
import edit_menu
import format_menu
import help_menu

# creating a tkinter window
root = Tk()

# gives the window a title and dimensions
root.title("TextEditor-newfile")
root.geometry("300x250+300+300")
root.minsize(width=400, height=400)

# i don't really know how to explain what this code does, but yeah it's important
text = ScrolledText(root, state='normal', height=400, width=400, wrap='word', pady=2, padx=3, undo=True)
text.pack(fill=Y, expand=1)
text.focus_set()

# creating a menubar
menubar = Menu(root)

# adding our menus to the menubar
file_menu.main(root, text, menubar)
edit_menu.main(root, text, menubar)
format_menu.main(root, text, menubar)
help_menu.main(root, text, menubar)

# running the whole program
root.mainloop()