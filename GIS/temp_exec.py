# -*- coding: utf-8 -*-
from Tkinter import *
import tkFileDialog, tkMessageBox
import os
import shapefile as shp
import Tkinter as tk
from ttk import *
import ttk as ttk
import draw, shp
import Image, ImageDraw

def Browse():
	paths=tkFileDialog.askopenfilenames()
	Dir_parent=os.path.dirname(paths[0])
	e1.delete(0, END)
	e1.insert(0, Dir_parent)
	DirSave=os.path.join(Dir_parent, 'pic')
	Dirshp=os.path.join(Dir_parent, 'shapefile')
	if not os.path.exists(DirSave):
		os.makedirs(DirSave)
	if not os.path.exists(Dirshp):
		os.makedirs(Dirshp)
	print DirSave
	unit, row, col= 5, 360, 200 #5, 360, 200
	im=Image.new('RGBA', (unit*col,unit*row))
	lowerbound=15
	for p in paths:
		#print 'start draw',p
		draw.Create_draw(p, DirSave)
		draw.Combine_draw(p, im, lowerbound)
	base=Image.open("base.png")
	im.paste(base, (1*unit,1*unit), base)
	im.save(str(lowerbound)+".png")

	#	print 'finish draw, and start shp'
	#	shp.Create_shp(p, Dirshp)
	Exit=tkMessageBox.askyesno("Loaction", 'Result: \n'+DirSave+'\n\nclick Yes to Exit')
	if Exit:
		win.quit()
	
win=tk.Tk()
win.title('Template pic_')

F1=ttk.LabelFrame(win, text=' Select File ', width=320)
F1.grid(row=0, padx=10, ipadx=5, ipady=5)

L1=tk.Label(F1, text='Path: ')
L1.grid(row=0, column=0,padx=(5,0))
e1=ttk.Entry(F1)
e1.grid(row=0, column=1, padx=5, pady=5, ipadx=5, ipady=5)
btn=ttk.Button(F1, text='Browse..', command=Browse).grid(row=0, column=2)

colorRamp={0:(39,117,121),1:(35,122,150),2:(48,135,162),3:(64,152,175),4:(81,158,186),5:(74,154,181),6:(102,183,200),7:(124,196,208),8:(135,202,219),9:(158,211,229),10:(159,223,235),11:(179,239,247),12:(18,144,80),13:(23,146,79),14:(50,157,85),15:(62,168,96),16:(79,172,102),17:(102,183,116),18:(125,192,121),19:(132,201,118),20:(147,212,130),21:(165,219,131),22:(186,226,137),23:(199,233,139),24:(211,238,145),25:(245,242,189),26:(242,233,140),27:(250,211,132),28:(242,197,94),29:(239,179,69),30:(230,159,53),31:(233,134,41),32:(234,120,8),33:(223,82,39),34:(235,19,92),35:(176,5,50),36:(114,6,0),37:(163,107,152),38:(132,82,153),39:(125,35,159)}

W=Canvas(win, width=320, height=10)
W.grid(row=1)

F2=ttk.LabelFrame(win, text=' Setting ', width=320)
F2.grid(row=2, padx=10, ipadx=5, ipady=5)
L21=tk.Label(F2, text='Upper bound: ')
L21.grid(row=0, column=0, padx=(5,0))
e21=ttk.Entry(F2)
e21.grid(row=0, column=1, padx=(5,0), pady=5, ipadx=5, ipady=5)
L212=tk.Label(F2, text='℃/mm')
L212.grid(row=0, column=2)

for key in sorted(colorRamp):
	c='#%02x%02x%02x' % colorRamp[key]
	W.create_rectangle(8*key, 0, 8+8*key, 80, outline=c, fill=c)

win.mainloop()	
