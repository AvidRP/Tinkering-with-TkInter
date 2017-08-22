from Tkinter import *
import tkMessageBox

#Message Box

root = Tk()

#This is like alert from js
tkMessageBox.showinfo("Window Title", 'This is the message param')

answer = tkMessageBox.askquestion('Question 1', 'Enter site')

if(answer == 'yes'):
    print("Enter Site")
else:
    root.quit()

root.mainloop()



