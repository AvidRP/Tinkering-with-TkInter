from Tkinter import *

#mouse click events

root = Tk()

def leftClick(event):
    print("Left")


def rightClick(event):
    print("Right")

frame = Frame(root, width = 400, height=400)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button>", rightClick)
frame.pack()

root.mainloop()