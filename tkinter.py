from Tkinter import *

#using tkinter grid instead of just the pack func

root = Tk()

theLabel = Label(root, text="Username")
theEntry = Entry(root, text="Enter your username")


theLabel2 = Label(root, text="Password")
theEntry2 = Entry(root, text="Password")


#Now using the grid to place items
#sticky is like text-align
# it takes the value N E S W for north south east west
theLabel.grid(row=0, sticky=E)
theLabel2.grid(row=1, sticky=E)
theEntry.grid(row=0,column=1)
theEntry2.grid(row=1, column=1)

checkBox = Checkbutton(root, text="Keep me signed in")
#so that the checkbox takes two column spaces
checkBox.grid(columnspan=2)


root.mainloop()