from Tkinter import *
import Tkinter as tk
import tkFileDialog

def clickCalc(path):
	print path
	with open(path)as file:
		lines=file.read().splitlines()
	count =0
	Date=[]; SRAD=[]; Tmax=[]; Tmin=[]; Rain=[]
	for line in lines:
		if count >4:
			tmp=line.split()
			Date.append(tmp[0])
			SRAD.append(float(tmp[1]))
			Tmax.append(float(tmp[2]))
			Tmin.append(float(tmp[3]))
			Rain.append(float(tmp[4]))
		count=count+1
	print "Tmax: ",sum(Tmax)
	print "Tmin: ",sum(Tmin)
	print "Rain: ",sum(Rain)

def clickBrowse():
	global path
	path=tkFileDialog.askopenfilename()
	e1.insert(10,path)
def test(path):
	print "PATH: ",path
	if len(path) >2:
		clickCalc(path)
def callback():
	print "clicked!"

path=""
win=Tk()
win.title("Ecocrop test app")
Label(win, text="path: ").grid(row=0)
e1 = Entry(win)
e1.grid(row=0,column=1)
button=Button(win, text="Browse", command=clickBrowse).grid(row=0,column=2)
button2=Button(win, text="Calculate", command=test(path)).grid(row=1,column=2)
button3=Button(win, text="QUIT", fg="red", command=win.quit).grid(row=1,column=3)

b=Button(text="click me",command=callback)
win.mainloop()

#clickCalc(path)


#path=tkFileDialog.askopenfilename()
#print path


