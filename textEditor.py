# Here is my first try at a GUI in Python, using the YouTube tutorial by DiogoTheCoder
# This script can create a new file, save As, open saved files, and Exit(Quit)

from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox
import tkinter.scrolledtext as ScrolledText

#root for main window
root = Tk(className = "Text Editor")
textArea = ScrolledText.ScrolledText(root, width = 100, height = 80)

#
# Functions
#

def openFile():
    file = filedialog.askopenfile(parent=root, title='select a text file', filetypes=(("Text file", "*.txt"),("All files", "*.*")))

    if file != None:
        contents = file.read()
        textArea.insert('1.0', contents)
        file.close()

def saveFile():
    file = filedialog.asksaveasfile(mode='w')

    if file != None:
        # slice off last char from get, bc extra return is added
        data = textArea.get('1.0', END+'-1c')
        file.write(data)
        file.close()

def exitRoot():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        root.destroy()
#
#
#
    
#menu options
menu = Menu(root)
root.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="SaveAs", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Quit", command=exitRoot)
textArea.pack()

#keep window open
root.mainloop()
