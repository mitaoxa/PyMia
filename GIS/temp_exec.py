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
import draw_town as town
import draw_mask as Mask
from tkColorChooser import askcolor
paths = None
def Browse():
	global paths
	paths=tkFileDialog.askopenfilenames()
	e1.delete(0, END)
	e1.insert(0, paths)

def ana():
	tmp=askcolor()
	global paths
	lowerbound=int(E_bound.get())
	Dir_parent=os.path.dirname(paths[0])
	DirSave=os.path.join(Dir_parent, 'output_'+str(lowerbound))
	ImgSave=os.path.join(DirSave, str(lowerbound)+".png")
	Dirshp=os.path.join(DirSave, 'shapefile_'+str(lowerbound))
	if not os.path.exists(DirSave):
		os.makedirs(DirSave)
	if not os.path.exists(Dirshp):
		os.makedirs(Dirshp)
	print DirSave
	unit, row, col= 5, 360, 200 #5, 360, 200
	im=Image.new('RGBA', (unit*col,unit*row))
	result={}
	for p in paths:
		#print 'finish draw, and start shp'
		#shp.Create_shp(p, Dirshp, lowerbound)
		shp.CombineShp(p, lowerbound, result)
	
		#print 'start draw',p
		#draw.Create_draw(p, DirSave, lowerbound)
		draw.Combine_draw(p, im, lowerbound)
	savePath=os.path.join(Dirshp,'Combine_temp_'+str(lowerbound)+'.shp')
	print 'result: ',len(result)
	shp.outputShp(result, savePath)
	base=Image.open(E_town.get())
	mask=Image.open(E_mask.get())
	im.paste((0, 0, 0, 0), (1*unit, 1*unit), mask)
	im.paste(base, (1*unit,1*unit), base)
	im.save(ImgSave)
	Exit=tkMessageBox.askyesno("Loaction", 'Result: \n'+DirSave+'\n\nclick Yes to Exit')
	if Exit:
		win.quit()

def checkTown():
	print 'check town here!'
	townpath=tkFileDialog.askopenfilename()
	if len(townpath) >6:
		E_town.delete(0, END)
		E_town.insert(0, townpath)
		Towntype=townpath[len(townpath)-3:]
		if Towntype == 'png' and townpath[len(townpath)-8:]=='base.png':
			LEDt.create_oval(0,0,10,10, fill='green')
		elif Towntype == 'shp':
			LEDt.create_oval(0,0,10,10, fill='orange')
			im=Image.new('RGBA', (5*200, 5*360))
			town.DrawTown(im)
			towndir=os.path.dirname(townpath)
			base=os.path.join(towndir, 'base.png')
			im.save(base)
			E_town.delete(0, END)
			E_town.insert(0, base)
			LEDt.create_oval(0,0,10,10, fill='green')
		else:
			LEDt.create_oval(0,0,10,10, fill='red')
def checkMask():
	print 'check mask here!'
	maskpath=tkFileDialog.askopenfilename()
	if len(maskpath) >6:
		E_mask.delete(0, END)
		E_mask.insert(0, maskpath)
		Masktype=maskpath[len(maskpath)-3:]
		if Masktype == 'png' and maskpath[len(maskpath)-8:]=='mask.png':
			LEDm.create_oval(0,0,10,10, fill='green')
		elif Masktype == 'txt':
                        LEDm.create_oval(0,0,10,10, fill='orange')
			im=Image.new('RGBA', (5*200, 5*360))
			Mask.DrawMask(im, maskpath)
			mask=os.path.join(os.path.dirname(maskpath), 'mask.png')
			im.save(mask)
			E_mask.delete(0, END)
			E_mask.insert(0, mask)
			LEDm.create_oval(0,0,10,10, fill='green')
		else:
			LEDm.create_oval(0,0,10,10, fill='red')


def setColor():
	global C
	color = askcolor()
	print color
	if not color[0] == None:
		C=color[0]
	btn_color.configure(bg=color[1])
	print C
win=tk.Tk()
win.title('Template pic_')

# Town File
F_town=ttk.LabelFrame(win, text=' Town File ', width=320)
F_town.grid(row=0,  ipadx=5, ipady=5)
LEDt=Canvas(F_town, width=10, height=10)
LEDt.grid(row=0, column=0, padx=5, pady=5)
LEDt.create_oval(0,0,10,10, fill='red')
E_town=ttk.Entry(F_town)
E_town.grid(row=0, column=1, padx=5, pady=5, ipadx=5, ipady=5)
btn_town=ttk.Button(F_town, text='Browse..', command=checkTown).grid(row=0, column=2)

# Mask File
F_mask=ttk.LabelFrame(win, text=' Mask File ', width=320)
F_mask.grid(row=1, padx=10, ipadx=5, ipady=5)
LEDm=Canvas(F_mask, width=10, height=10)
LEDm.grid(row=0, column=0, padx=5, pady=5)
LEDm.create_oval(0,0,10,10, fill='red')
E_mask=ttk.Entry(F_mask)
E_mask.grid(row=0, column=1, padx=5, pady=5, ipadx=5, ipady=5)
btn_town=ttk.Button(F_mask, text='Browse..', command=checkMask).grid(row=0, column=2)

# temp File
F1=ttk.LabelFrame(win, text=' Select File ', width=320)
F1.grid(row=2, padx=10, ipadx=5, ipady=5)

L1=tk.Label(F1, text='Path')
L1.grid(row=0, column=0,padx=(2,0))
e1=ttk.Entry(F1)
e1.grid(row=0, column=1, padx=2, pady=2, ipadx=5, ipady=5)
btn=ttk.Button(F1, text='Browse..', command=Browse).grid(row=0, column=2)

# draw Canvas 
colorRamp={0:(39,117,121),1:(35,122,150),2:(48,135,162),3:(64,152,175),4:(81,158,186),5:(74,154,181),6:(102,183,200),7:(124,196,208),8:(135,202,219),9:(158,211,229),10:(159,223,235),11:(179,239,247),12:(18,144,80),13:(23,146,79),14:(50,157,85),15:(62,168,96),16:(79,172,102),17:(102,183,116),18:(125,192,121),19:(132,201,118),20:(147,212,130),21:(165,219,131),22:(186,226,137),23:(199,233,139),24:(211,238,145),25:(245,242,189),26:(242,233,140),27:(250,211,132),28:(242,197,94),29:(239,179,69),30:(230,159,53),31:(233,134,41),32:(234,120,8),33:(223,82,39),34:(235,19,92),35:(176,5,50),36:(114,6,0),37:(163,107,152),38:(132,82,153),39:(125,35,159)}
defaultColor='#%02x%02x%02x' % colorRamp[0]
global C
C=colorRamp[0]

W=Canvas(win, width=320, height=5)
W.grid(row=5)

F2=ttk.LabelFrame(win, text=' Setting ', width=320)
F2.grid(row=4, padx=10, ipadx=5, ipady=5)
L21=tk.Label(F2, text='Upper bound')
L21.grid(row=0, column=0, padx=(5,0))
E_bound=ttk.Entry(F2)
E_bound.grid(row=0, column=1, padx=(5,0), pady=5, ipadx=5, ipady=5)
L212=tk.Label(F2, text='℃')
L212.grid(row=0, column=2)
btn_color=tk.Button(F2, command=setColor, bg=defaultColor)
btn_color.grid(row=0, column=3)

# analsys button
btn_ana=ttk.Button(win, text='Analsys', command=ana).grid(row=6, padx=10, pady=10, ipadx=110, ipady=2)


for key in sorted(colorRamp):
	c='#%02x%02x%02x' % colorRamp[key]
	W.create_rectangle(8*key, 0, 8+8*key, 80, outline=c, fill=c)


win.mainloop()
