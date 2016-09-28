from Tkinter import *
import tkFileDialog
from ttk import * 

def click():
	print "!!!"

def ClickBrowse():
	path=tkFileDialog.askopenfilename()
	e1.insert(10,path)

def ClickCalc():
	path=e1.get()
	print "click calc: <",path,">"
	with open(path) as file:
		lines=file.read().splitlines()
	count=0
	Date=[]; SRAD=[]; Tmax=[]; Tmin=[]; Rain=[]
	for line in lines:
		if count>4:
			tmp=line.split()
			Date.append(tmp[0])
			SRAD.append(float(tmp[1]))
			Tmax.append(float(tmp[2]))
			Tmin.append(float(tmp[3]))
			Rain.append(float(tmp[4]))
		count=count+1
	print "Tmax: ", sum(Tmax)
	print "Tmin: ", sum(Tmin)
	print "Rain: ", sum(Rain)


win=Tk()
win.title("EcoCrop")
label=Label(win, text="PATH: ").grid(row=0)
e1 = Entry(win)
e1.grid(row=0, column=1)
BT001=Button(win, text="Browse", command=ClickBrowse).grid(row=0, column=2)
label2=Label(win, text="RESULT").grid(row=1,column=0)
tmpTxt=Text(win,height=6, width=20)
tmpTxt.grid(row=1, column=1)
BT002=Button(win, text="Calculate", command=ClickCalc).grid(row=2, column=0)
BTquit=Button(win, text="QUIT", command=win.quit).grid(row=2, column=1)
win.mainloop()
