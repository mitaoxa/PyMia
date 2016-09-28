from __future__ import division #let division can output float
from Tkinter import*
import Tkinter as tk
from ttk import *
import ttk as ttk
import tkFileDialog
import os

def Browse():
	path=tkFileDialog.askdirectory()
	e1.delete(0, END)
	e1.insert(0, path)
	for root, dirnames, filenames in os.walk(path):
		files=filenames
		break
	print len(files)
	SS.set(' '+str(len(files))+' files is selected')	

	# ###################################### #
	#		  LAYOUT  		 #
	# ###################################### #

win=tk.Tk()
win.title("Ecocrop")


# DIREACTORY #
F1=ttk.LabelFrame(win, text=' Choose  Directory ')
F1.grid(row=0, sticky=W, padx=10, pady=5, ipadx=5, ipady=5)

L1=tk.Label(F1, text='select: ')
L1.grid(row=0, column=0)
e1=tk.Entry(F1)
e1.grid(row=0, column=1, padx=5, pady=5, ipadx=5, ipady=5)
btn1=tk.Button(F1, text='Browse..', command=Browse).grid(row=0, column=2)

# SETUP INFO #
pane=ttk.PanedWindow(win, orient=HORIZONTAL)
pane.grid(row=3, padx=5, pady=7)

Ft=tk.LabelFrame(pane, text='Template', relief=SUNKEN)
name=['min', 'max', 'opmin', 'opmax']
Fn={'T':'Template', 'R':'Rain'}
liter=['T', 'R']
F={}; L={}; E={}
Crow=0
for l in liter:
	F[l]=ttk.LabelFrame(pane, text=Fn[l], relief=SUNKEN)
	Crow=0
	for n in name:
		tmp=l+n
		L[tmp]=tk.Label(F[l], text=' '+tmp+' ').grid(row=Crow, column=0, padx=1, pady=1)
		E[tmp]=tk.Entry(F[l], width=4)
		E[tmp].grid(row=Crow, column=1, padx=3, pady=1)
		Crow=Crow+1
	pane.add(F[l])

F['suit']=ttk.LabelFrame(pane, text=' Date ', relief=SUNKEN)
L['t1']=tk.Label(F['suit'], text='Tsuit I').grid(row=0,columnspan=3, padx=3, pady=1)
E['t11']=tk.Entry(F['suit'], width=3)
E['t11'].grid(row=1, column=0)
L['t12]']=tk.Label(F['suit'], text='~').grid(row=1, column=1)
E['t12']=tk.Entry(F['suit'],width=3)
E['t12'].grid(row=1, column=2)

L['t2']=tk.Label(F['suit'],text='Tsuit II').grid(row=2, columnspan=3, padx=3, pady=1)
E['t21']=tk.Entry(F['suit'],width=3)
E['t21'].grid(row=3, column=0, padx=2)
L['t21']=tk.Label(F['suit'], text='~').grid(row=3, column=1)
E['t22']=tk.Entry(F['suit'], width=3)
E['t22'].grid(row=3, column=2, padx=2)
pane.add(F['suit'])
		###   initial   ###
index={'Tmin': 10, 'Tmax':30, 'Topmin': 22, 'Topmax':26, 't11':52, 't12':171, 't21': 182, 't22':304, 'Rmin': 1000, 'Rmax':4000, 'Ropmin':1500,'Ropmax':2000}
for key,value in index.iteritems():
	E[key].insert(END, value)

# QUIT #
BTN_QUIT=tk.Button(win, text='QUIT', comman=win.quit, width='40').grid(row=4)

# STATUS BAR #	
SS = StringVar()
status=ttk.Label(win, textvariable=SS, relief=SUNKEN, width=40)
status.grid(sticky='SWE', padx=2, pady=1)
win.mainloop()

