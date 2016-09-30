from __future__ import division #let division can outupt float
from Tkinter import *
import Tkinter as tk
from ttk import *
import ttk as ttk
import tkFileDialog


win=tk.Tk()
win.title("Ecocrop")
#win.iconbitmap(r'fao5.ico')
def Browse():

	path=tkFileDialog.askopenfilename()
	e1.delete(0,END)
	e1.insert(0,path)
	try:
		with open(path) as file:
			lines=file.read().splitlines()
	except IOError:
		SS.set("Please select a file path!")
	tmp=lines[3].split()
	info={"INSI":tmp[0], "LAT":tmp[1], "LONG":tmp[2], "ELEV":tmp[3], "TAV":tmp[4], "AMP":tmp[5], "RFHT":tmp[6], "WDHT":tmp[7]}			
	Finfo = ttk.LabelFrame(win, text="  info  ")
	Finfo.grid(row=1, columnspan=8, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)
	count=0
	Linfo=[range(0,11)]
	LinfoDetail=[range(0,11)]
	for key, value in info.iteritems():
		print "(",count,") ",key, " ->",value
		Linfo.append(tk.Label(Finfo, text=key,width=6).grid(row=0, column=count, sticky='W'))
		LinfoDetail.append(tk.Label(Finfo, text=value, width=6).grid(row=1, column=count, sticky='W'))
		count=count+1

def ClickAna():
	
	win.geometry('505x535')
	path=e1.get()
	if  len(path)<=0:
		SS.set("path is empty!")
		
	if len(eTmin.get())<=0 or len(eTmax.get())<=0 or len(eTopmin.get())<=0 or len(eTopmax.get())<=0 \
		or len(eTs1.get())<=0   or len(eTs11.get())<=0 or len (eTs2.get())<=0 or len(eTs22.get())<=0  \
		or len(ERmin.get())<=0 or len(ERmax.get())<=0 or len(ERopmax.get())<=0 or len(ERopmin.get()) <=0:
		print "Something is empty"
		SS.set("something is empty")
		return
	else:
		try :
			Tmin=float(eTmin.get())
			Tmax=float(eTmax.get())
			Topmin=float(eTopmin.get())
			Topmax=float(eTopmax.get())
			suitS1=int(eTs1.get())
			suitE1=int(eTs11.get())
			suitS2=int(eTs2.get())
			suitE2=int(eTs22.get())
			Rmin=float(ERmin.get())
			Rmax=float(ERmax.get())
			Ropmin=float(ERopmin.get())
			Ropmax=float(ERopmax.get())
			SS.set("")
		except ValueError:
			SS.set("please type in number!")
	print "click calc: <", path,">"
	with open(path) as file:
		lines=file.read().splitlines()
	count=0	
	mDate=[]; mSRAD=[]; fileTmax=[]; fileTmin=[]; fileRain=[] #mean count from file
	for line in lines:
		if count>4:
			tmp=line.split()
			mDate.append(tmp[0])
			mSRAD.append(float(tmp[1]))
			fileTmax.append(float(tmp[2]))
			fileTmin.append(float(tmp[3]))
			fileRain.append(float(tmp[4]))
		count=count+1

	Mtless=(-100.0)/(Tmin-Topmin)
	print "Mt: ",Mtless
	Lm1=tk.Label(FI1, text="Mt: "+str('%.2f' % Mtless)).grid(row=0, column=0, sticky=W)
	Atless=-(Mtless)*Tmin
	print "At: ",Atless
	Lm2=tk.Label(FI1, text="At: "+str('%.2f' % Atless)).grid(row=1, column=0, sticky=W)
	Mtmore=(-100)/(Tmax-Topmax)
	print "Mt2: ",Mtmore
	Lm3=tk.Label(FI1, text="Mt: "+str('%.2f' % Mtmore)).grid(row=2, column=0, sticky=W)
	Atmore=-(Mtmore)*Tmax
	print "At2: ",Atmore
	Lm4=tk.Label(FI1, text="At: "+str('%.2f' % Atmore)).grid(row=3, column=0, sticky=W)
	
	RMtless=(-100.0)/(Rmin-Ropmin)
	print "RMt: ",RMtless
	Lm5=tk.Label(FI2, text="Mt: "+str('%.2f' % RMtless)).grid(row=0, column=0, sticky=W)
	RAtless=-(RMtless)*Rmin
	print "At: ",RAtless
	Lm6=tk.Label(FI2, text="At: "+str('%.2f' % RAtless)).grid(row=1, column=0, sticky=W)
	RMtmore=(-100)/(Rmax-Ropmax)
	print "Mt2: ",RMtmore
	Lm7=tk.Label(FI2, text="Mt: "+str('%.2f' % RMtmore)).grid(row=2, column=0, sticky=W)
	RAtmore=-(RMtmore)*Rmax
	print "At2: ",RAtmore
	Lm8=tk.Label(FI2, text="At: "+str('%.2f' % RMtmore)).grid(row=3, column=0, sticky=W)
	
	count =0
	meanT=[]; Tsuit=[]
	while count<len(fileTmax):
		meanT.append((fileTmax[count]+fileTmin[count])/2)
#		print fileTmax[count], "+",fileTmin[count],"/2=",meanT[count]
		tmp=meanT[count]
		if tmp>=Topmin and tmp<=Topmax:
			Tsuit.append(100)
		elif tmp<Tmin or tmp>Tmax:
			Tsuit.append(0)
		elif tmp<Topmin and tmp>=Tmin:
			suit=Atless+Mtless*tmp
			Tsuit.append(suit)
		elif tmp>Topmax and tmp<=Tmax:
			suit=Atmore+Mtmore*tmp
			Tsuit.append(suit)
		else:
			print "####################### ERROR #########################"
		#print tmp,">",Tsuit[count]
		count=count+1
		S1=sum(Tsuit[(suitS1-1):suitE1])/(suitE1-suitS1+1)
		S2=sum(Tsuit[(suitS2-1):suitE2])/(suitE2-suitS2+1)
	print "suit1: (",suitS1,"~",suitE1,"): ",  S1
	print "suit2: (",suitS2,"~",suitE2,"): ",  S2
	Lm9=tk.Label(FI3, text="Tsuit 1" ).grid(row=0, column=0, sticky=W)
	Lm10=tk.Label(FI3, text=' = %.2f' % S1 ).grid(row=1, column=0, sticky=E)
	Lm11=tk.Label(FI3, text="Tsuit 2").grid(row=2, column=0, sticky=W)
	Lm12=tk.Label(FI3, text=' = %.2f' % S2 ).grid(row=3, column=0, sticky=E)
	
	
	count=0
	Rsuit=-1
	tmp=sum(fileRain)
	if tmp>=Ropmin and tmp <=Ropmax:
		Rsuit=100
	elif tmp<Rmin or tmp >Rmax:
		Rsuit=0
	elif tmp<Ropmin and tmp>=Rmin:
		suit=RAtless+RMtless*tmp
		Rsuit=suit
	elif tmp>Ropmax and tmp <=Rmax:
		suit=RAtmore+RMtmore*tmp
		Rsuit=suit
	else:
		print "####################### ERROR #########################"
	print  "Rain: ", tmp
	print  "Rsuit: ", Rsuit
	
	Lm13=tk.Label(FI4, text="Total Rain: ").grid(row=0, column=0, sticky=W)
	Lm14=tk.Label(FI4, text=str(tmp)).grid(row=1, column=0, sticky=E)
	Lm15=tk.Label(FI4, text="Rain Suit: ").grid(row=2, column=0, sticky=W)
	Lm16=tk.Label(FI4, text=str(Rsuit)).grid(row=3, column=0, sticky=E)
		
# ###################
#  LAYOUT		            #
# ###################
F1 =ttk.LabelFrame(win, text='1. Choose File: ')
F1.grid(row=0, columnspan=8, sticky='W', padx=10, pady=5, ipadx=5, ipady=5)

L1=tk.Label(F1, text="Select Files: ")
L1.grid(row=0, column=0)
e1=tk.Entry(F1, width=30)
e1.grid(row=0, column=1,columnspan=2 ,padx=5, pady=5, ipadx=5, ipady=5)
BTN1=tk.Button(F1,text="Browse..",command=Browse).grid(row=0, column=3)

Fsu = ttk.LabelFrame(win, text="Model SetUp")
Fsu.grid(row=2, columnspan=8, sticky='W', padx=5,pady=5, ipadx=5)
eTmin=tk.Entry(Fsu, width=7,text="10")
eTmin.grid(row=0,column=1)
eTmin.insert(END, '10')
eTmax=tk.Entry(Fsu, width=7)
eTmax.grid(row=0,column=3)
eTmax.insert(END, '36')
eTopmin=tk.Entry(Fsu, width=7)
eTopmin.grid(row=0, column=5)
eTopmin.insert(END, '22')
eTopmax=tk.Entry(Fsu, width=7)
eTopmax.grid(row=0, column=7)
eTopmax.insert(END, '26')


eTs1=tk.Entry(Fsu, width=7)
eTs1.grid(row=2, column=1)
eTs11=tk.Entry(Fsu, width=7)
eTs11.grid(row=2, column=3)
eTs1.insert(END, 52)
eTs11.insert(END,171)

eTs2=tk.Entry(Fsu, width=7)
eTs2.grid(row=2, column=5)
eTs22=tk.Entry(Fsu, width=7)
eTs22.grid(row=2, column=7)
eTs2.insert(END, 182)
eTs22.insert(END, 304)

LTmin=tk.Label(Fsu, text="Tmin").grid(row=0,column=0)
LTmax=tk.Label(Fsu, text="Tmax").grid(row=0,column=2)
LTopmin=tk.Label(Fsu, text="Topmin").grid(row=0,column=4)
LTopmax=tk.Label(Fsu, text="Topmax").grid(row=0,column=6)
LRmin=tk.Label(Fsu, text="Rmin").grid(row=1,column=0)
ERmin=tk.Entry(Fsu, width=7)
ERmin.grid(row=1,column=1)
ERmin.insert(END, 1000)
LRmax=tk.Label(Fsu, text="Rmax").grid(row=1,column=2)
ERmax=tk.Entry(Fsu, width=7)
ERmax.grid(row=1,column=3)
ERmax.insert(END,4000)
LRopmin=tk.Label(Fsu, text="Ropmin").grid(row=1,column=4)
ERopmin=tk.Entry(Fsu, width=7)
ERopmin.grid(row=1,column=5)
ERopmin.insert(END,1500)
LRopmax=tk.Label(Fsu, text="Ropmax").grid(row=1,column=6)
ERopmax=tk.Entry(Fsu, width=7)
ERopmax.grid(row=1,column=7)
ERopmax.insert(END, 2000)
LTs1=tk.Label(Fsu, text="Tsuit1").grid(row=2, column=0)
LTs11=tk.Label(Fsu, text="~").grid(row=2, column=2)
LTs2=tk.Label(Fsu, text="Tsuit2").grid(row=2, column=4)
LTs22=tk.Label(Fsu, text="~").grid(row=2, column=6)

BTN_Analysis=tk.Button(Fsu,text="ANALYSIS", command=ClickAna, width=40).grid(row=3, column=0, columnspan=8, pady=10)


p=ttk.PanedWindow(win, orient=HORIZONTAL)
p.grid(row=3, columnspan=8, padx=5, pady=7)


FI1=tk.LabelFrame(p, text='TEMP Interal ', relief=SUNKEN)    # intertal here ##########################
top=tk.Label(FI1,text="").grid(row=0, column=0)
p.add(FI1)
FI2=tk.LabelFrame(p, text='RAIN Interal ', relief=SUNKEN)
down=tk.Label(FI2, text="").grid(row=0, column=0)
p.add(FI2)
FI3=tk.LabelFrame(p, text=' Tsuit I & II ', relief=SUNKEN)
top=tk.Label(FI3,text="").grid(row=0, column=0)
p.add(FI3)
FI4=tk.LabelFrame(p, text=' Rain Suit  ', relief=SUNKEN)
down=tk.Label(FI4, text="").grid(row=0, column=0)
p.add(FI4)
"""
FMS = ttk.LabelFrame(p, text="RESULT (total)")
FMS.grid(row=3, columnspan=8, sticky='W',padx=25, pady=5, ipadx=25, ipady=5)
p.add(FMS)

L21 = tk.Label(FMS, text="Tmax ", width=7).grid(row=0, column=0, sticky='W')
e211=tk.Entry(FMS,width=15, text="")
e211.grid(row=0,column=1, sticky='W')
#L211= tk.Label(F2, text="", width=10).grid(row=0, column=1, sticky='W')
L212= tk.Label(FMS, text=" C", width=8).grid(row=0, column=2, sticky='W')
L22 = tk.Label(FMS, text="Tmin ",width=7).grid(row=1, column=0, sticky='W')
#L221= tk.Label(F2, text="", width=10).grid(row=1, column=1, sticky='W')
e221= tk.Entry(FMS, width=15)
e221.grid(row=1,column=1, sticky='W')
L222= tk.Label(FMS, text=" C", width=8).grid(row=1,column=2, sticky='W')
L23 = tk.Label(FMS, text="Rain ",width=7).grid(row=2, column=0, sticky= 'W')
#L231= tk.Label(F2, text="", width=10).grid(row=2, column=1, sticky='W')
e231= tk.Entry(FMS, width=15)
e231.grid(row=2, column=1, sticky='W')
L232= tk.Label(FMS, text=" mm", width=8).grid(row=2, column=2, sticky='W')
"""
BTN_QUIT=tk.Button(win, text="QUIT", command=win.quit, width="40", bg='red', fg='white').grid(row=4, columnspan=8)

SS=StringVar()


status=ttk.Label(win, textvariable=SS, relief="sunken", width=55)
status.grid(sticky='SWE', padx=2, pady=1)

win.mainloop()
