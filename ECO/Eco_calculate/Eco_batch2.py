from __future__ import division #let division can output float
from Tkinter import*
import Tkinter as tk
from ttk import *
import ttk as ttk
import tkFileDialog
import os
import Eco_calc as eco

def Browse():
	eco.Browse(e1, SS)
def ANA():
#	SS.set(' Click analsys button')
#	B.ANA(SS)
	eco.Analsys(e1.get(), E, SS)
	# ###################################### #
	#		  LAYOUT  		 #
	# ###################################### #

win=tk.Tk()
win.title("Ecocrop")


# DIREACTORY #
F1=ttk.LabelFrame(win, text=' Choose  Directory ')
F1.grid(row=0, sticky=W, padx=10, pady=5, ipadx=5, ipady=5)

L1=tk.Label(F1, text=' Select: ')
L1.grid(row=0, column=0)
e1=tk.Entry(F1)
e1.grid(row=0, column=1, padx=5, pady=5, ipadx=5, ipady=5)
btn1=tk.Button(F1, text='Browse..', command=Browse).grid(row=0, column=2)

# SETUP INFO #
pane=ttk.PanedWindow(win, orient=HORIZONTAL)
pane.grid(row=1, padx=5, pady=7)

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
E['Tsuit1-1']=tk.Entry(F['suit'], width=3)
E['Tsuit1-1'].grid(row=1, column=0, padx=(5,0))
L['t12]']=tk.Label(F['suit'], text='~').grid(row=1, column=1)
E['Tsuit1-2']=tk.Entry(F['suit'],width=3)
E['Tsuit1-2'].grid(row=1, column=2, padx=(0,5))

L['t2']=tk.Label(F['suit'],text='Tsuit II').grid(row=2, columnspan=3, padx=3, pady=1)
E['Tsuit2-1']=tk.Entry(F['suit'],width=3)
E['Tsuit2-1'].grid(row=3, column=0, padx=(5,0))
L['t21']=tk.Label(F['suit'], text='~').grid(row=3, column=1)
E['Tsuit2-2']=tk.Entry(F['suit'], width=3)
E['Tsuit2-2'].grid(row=3, column=2, padx=(0,5))
pane.add(F['suit'])
		###   initial   ###
index={'Tmin': 10, 'Tmax':36, 'Topmin': 22, 'Topmax':26, \
	'Tsuit1-1':52, 	'Tsuit1-2':171, 'Tsuit2-1': 182, 'Tsuit2-2':304,\
	 'Rmin': 1000, 'Rmax':4000, 'Ropmin':1500,'Ropmax':2000}
for key,value in index.iteritems():
	E[key].insert(END, value)
# tmp notebook #
n=ttk.Notebook(win)
n.grid(row=2, columnspan=3)
f1=ttk.Frame(n, height=20, width=100)
f2=ttk.Frame(n)
n.add(f1, text='one')
n.add(f2, text='two')

# ANALSYS #
BTN_ANA=tk.Button(win, text='ANALSYS', command=ANA, width='40').grid(row=3)
# QUIT #
BTN_QUIT=tk.Button(win, text='QUIT', command=win.quit, width='40').grid(row=4)

# STATUS BAR #	
SS = StringVar()
status=ttk.Label(win, textvariable=SS, relief=SUNKEN, width=40)
status.grid(sticky='SWE', padx=2, pady=1)
win.mainloop()

