from Tkinter import *

# need to build a basic window first
# so that we know where to place widgets

#obj creation from tk class store it in root
root = Tk() #blank window

# root.minsize(width="400", height= "400")

#frames act like invisible containers
topFrame = Frame(root)
#to display frame: (anytime wanna display sth gotta pack
#by default its packs at the top
topFrame.pack()

bottomFrame = Frame(root)
#we wanna specify where we pack the bottomFrame in our window
bottomFrame.pack(side=BOTTOM)

#putting some widgets in there
firstButton = Button(topFrame, text="Click here", fg = "green")
secondButton = Button(topFrame, text="Click here", fg = "red")
thirdButton = Button(topFrame, text="Click here", fg = "blue")
fourthButton = Button(bottomFrame, text="Click here", fg = "yellow")

#by default things get packed on top of each other
firstButton.pack(side = LEFT)
secondButton.pack(side = LEFT)
thirdButton.pack(side = LEFT)
fourthButton.pack(side = TOP)

#need mainloop to run the program till the user closes it
#so it gives us time to actually view it
root.mainloop()

