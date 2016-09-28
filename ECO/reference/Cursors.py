from Tkinter import *
import Tkinter

# more in http://www.tutorialspoint.com/python/tk_cursors.htm

top = Tkinter.Tk()

B1 = Tkinter.Button(top, text ="circle", relief=RAISED,\
                         cursor="circle")
B2 = Tkinter.Button(top, text ="plus", relief=RAISED,\
                         cursor="plus")
B1.pack()
B2.pack()
top.mainloop()