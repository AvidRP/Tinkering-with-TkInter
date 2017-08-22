from Tkinter import *

#Making statusbar

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

#======================================================================#
#Toolbar

toolbar = Frame(root)
insertButton = Button(toolbar, text="Insert Image", command=doSomething)
insertButton.pack(side=LEFT, padx=2, pady=2)

printButton = Button(toolbar, text="Print Image", command=doSomething)
printButton.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

#======================================================================#
#Statusbar
#
status = Label(root, text = "Display Static text status", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()



