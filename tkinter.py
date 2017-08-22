from Tkinter import *

#Drop down menus

def doSomething():
    print("Something")

root = Tk()

#making the actual menu bar that goes into the root window
menu = Menu(root)
#configuring the menu
root.config(menu=menu)

#Titles within the menu bar
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)

#Adding stuff to the drop down menu
subMenu.add_command(label="New Project...", command=doSomething)
subMenu.add_separator()
subMenu.add_command(label="New..", command=doSomething)

editMenu = Menu(menu)
menu.add_cascade(labe="Edit", menu=editMenu)
editMenu.add_command(label="Edit...")

root.mainloop()