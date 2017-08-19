from Tkinter import *

# need to build a basic window first
# so that we know where to place widgets

#obj creation from tk class store it in root
root = Tk() #blank window

#baisc text
#first param is where you want the text to go
#second is the text itself
theLabel = Label(root, text = "This is some text")
root.minsize(width="500", height="500")

#to actually display the text
#it just packs the text wherever it can
theLabel.pack()

#need mainloop to run the program till the user closes it
#so it gives us time to actually view it
root.mainloop()
