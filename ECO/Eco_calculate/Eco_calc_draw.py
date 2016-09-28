from __future__ import division
from Tkinter import *
import Tkinter as tk
import ttk as ttk
import os
import tkFileDialog
import Image, ImageDraw

def getFiles(path):
	for root, dirnames, filenames in os.walk(path):
		files=filenames
		return files

def Calc_(Mt, At, E, path, filename, SS):
	Tsuit=[]
	location={}; suit={}
	meanT=[]; Rain=[]
	with open(os.path.join(path,filename)) as file:
		lines=file.read().splitlines()
	detail=lines[3].split()
	suit['#']=int(filename[:4])
	suit['X']=detail[2]
	suit['Y']=detail[1]
#	suit['location']=location
	count=5
	for line in lines[5:]:
		tmp=line.split()
		meanT.append((float(tmp[2])+float(tmp[3]))/2)
		Rain.append(float(tmp[4]))
		count=count+1
	count=0
	while count<len(meanT):
		temp=meanT[count]
		if temp >= E['Topmin'] and temp <= E['Topmax']:
			Tsuit.append(100)
		elif temp < E['Tmin'] or temp > E['Tmax']:
			Tsuit.append(0)
		elif temp < E['Topmin'] and temp >= E['Tmin']:
			tmp=At['TLess']+Mt['TLess']*temp
			Tsuit.append(tmp)
		elif temp > E['Topmax'] and temp <= E['Tmax']:
			tmp=At['TMore']+Mt['TMore']*temp
			Tsuit.append(tmp)
		else:
			SS.set(' Calc_ ERROR: Template suit')
		count=count+1
	start=int(E['Tsuit1-1'])
	end=int(E['Tsuit1-2'])
	suit['TsuitI']=sum(Tsuit[(start-1):end])/(end-start+1)
	start=int(E['Tsuit2-1'])
	end=int(E['Tsuit2-2'])
	suit['TsuitII']=sum(Tsuit[(start-1):end])/(end-start+1)
	
	tmp=sum(Rain)
	if tmp >= E['Ropmin'] and tmp <= E['Ropmax']:
		Rsuit=100
	elif tmp < E['Rmin'] or tmp > E['Rmax']:
		Rsuit=0
	elif tmp < E['Ropmin'] and tmp >= E['Rmin']:
		Rsuit=At['RLess']+Mt['RLess']*tmp
	elif tmp > E['Ropmax'] and tmp <= E['Rmax']:
		Rsuit=At['RMore']+Mt['RMore']*tmp
	else:
		SS.set(' Calc_ ERROR: Rain suit')
	suit['Rsuit']=Rsuit
	suit['totalRain']=tmp
	
	return suit

def Analsys(path, E, SS):
	SS.set(' path: '+path)
	if len(path) <=0:
		SS.set(' path is empty!')
	flag=True
	value={}
	for key,entry in E.iteritems():
#		SS.set('')
		if len(entry.get()) <=0:
			SS.set(' Entry <'+key+'>: is empty')
			flag=False
		else:
			try:
				value[key]=float(entry.get())
			except ValueError:
				SS.set(' Entry <'+key+'>: please type in number')
				flag=False
	if flag==False:
		return 
	files=getFiles(path)
	index=['T','R']
	Mt={}; At={}
	for i in index:
		less=i+'Less'
		more=i+'More'
		Mt[less]=(-100)/(value[i+'min']-value[i+'opmin'])
		At[less]=-(Mt[less])*value[i+'min']
		Mt[more]=(-100)/(value[i+'max']-value[i+'opmax'])
		At[more]=-(Mt[more])*value[i+'max']
	record={}
	for f in files:
		suit=Calc_(Mt, At, value, path, f, SS)
		index=int(f[:4])
		record[index-1]=suit
	SS.set(' Calc_ finished')

	output=os.path.join(path, 'output')
	if not os.path.exists(output):
		os.makedirs(output)

	pic=os.path.join(path, 'pic')
	if not os.path.exists(pic):
		os.makedirs(pic)
	
	lmax,lmin,amax,amin=0,999,0,999
	for key,r in record.iteritems():
		if float(r['X'])>lmax:
			lmax=float(r['X'])
		if float(r['X'])<lmin:
			lmin=float(r['X'])
		if float(r['Y'])>amax:
			amax=float(r['Y'])
		if float(r['Y'])<amin:
			amin=float(r['Y'])

	print 'long <',lmax,'>, <',lmin,'>',str(round((lmax-lmin)/0.049))
	print 'lat <', amax,'>,<',amin,'>',str(round((amax-amin)/0.045))

	nl=int(round((lmax-lmin)/0.049))+1
	na=int(round((amax-amin)/0.045))+1
	unit=20
	im=Image.new('RGBA', (unit*nl,unit*na))
	D=ImageDraw.Draw(im)
	
	colorRamp={10:(62,168,96),9:(79,172,102),8:(102,183,116),7:(125,192,121),6:(132,201,118),5:(147,212,130),4:(165,219,131),3:(186,226,137),2:(199,233,139),1:(211,238,145),0:(245,242,189)}	
	flag=True
	for key, r in record.iteritems():
		suitI=int((r['TsuitI']*r['Rsuit'])/1000)
		if suitI == 0:
			color=colorRamp[0]
		else:
			color=colorRamp[suitI]
		X=int(round((float(r['X'])-lmin)/0.049))
		Y=int(round((amax-float(r['Y']))/0.045))
		if flag==True:
			flag=False
			print '-> ',X,', ',Y,'(',r['X'],',',r['Y']
	
		D.rectangle((X*unit,Y*unit,(X+1)*unit, (Y+1)*unit),fill=color)


	im.save(path[len(path)-4:]+'_suitI.png')

def Browse(E, SS):
	path=tkFileDialog.askdirectory()
	E.delete(0, END)
	E.insert(0, path)
	
	files=getFiles(path)
	print len(files)
	SS.set(' '+str(len(files))+' files in selected')


