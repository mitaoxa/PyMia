from Tkinter import *
import tkFileDialog
import os
import shapefile as shp
import Tkinter as tk
from ttk import *
import ttk as ttk
import os

global path
def Browse():
	global path
	print 'click browse'
	path=tkFileDialog.askopenfilename()
	e1.delete(0, END)
	e1.insert(0, path)

	
win=tk.Tk()
win.title('Template pic_')

F1=ttk.LabelFrame(win, text=' Select File ')
F1.grid(row=0, sticky=W, padx=10, pady=5, ipadx=5, ipady=5)

L1=tk.Label(F1, text='Path: ')
L1.grid(row=0, column=0)
e1=tk.Entry(F1)
e1.grid(row=0, column=1, padx=5, pady=5, ipadx=5, ipady=5)
btn=tk.Button(F1, text='Browse..', command=Browse).grid(row=0, column=2)



win.mainloop()	
"""
print 'path: <',path,'>'

with open(path) as file:
	lines=file.read().splitlines()

LONG, LAT=120.0, 25.47

count, index=0,0
point={}

for line in lines:
	if count==10:
		count=0
		index=index+1
	if index in point:
		point[index]+=' '+line
	else:
		point[index]=str(line)
	count=count+1

w=shp.Writer(shp.POLYGON)
w.autoBalance=1

w.field('ID', 'N')
w.field('X', 'F', 10, 8)
w.field('Y', 'F', 10, 8)
w.field('temp', 'F', 10, 8)
count=0

empty=point[0].split()

for key,value in point.iteritems():
	ps=value.split()
	for p in ps:
		if p != empty[0]:
			#left up -> right up -> right down -> left down
			loc=[LONG, LAT]
			LU=[LONG-0.005, LAT+0.005]
			RU=[LONG+0.005, LAT+0.005]
			RD=[LONG+0.005, LAT-0.005]
			LD=[LONG-0.005, LAT-0.005]
			par=[LU, RU, RD, LD, LU]
			w.poly(parts=[par])
			w.record(count, LONG, LAT, p)
#		w.point(LONG, LAT)
#		w.record(count, LONG, LAT, p)
		count=count+1
		LONG=LONG+0.01
	LAT=LAT-0.01
	LONG=120.0

filename=path[30:44]

dirname=os.path.dirname(path)
output=os.path.join(dirname,filename+'shp')

if not os.path.exists(output):
	os.makedirs(output)
path_shp=os.path.join(output,filename+'.shp')
w.save(path_shp)

print 'output file ',path_shp
"""	
