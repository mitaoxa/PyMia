from __future__ import division
from Tkinter import *
import Tkinter as tk
import ttk as ttk
import os
import tkFileDialog

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

	SS.set(' output: '+output+'/suit.csv')

	count=0
	with open(os.path.join(output, 'suit.csv'), 'w+') as file:
		file.write('FID,X,Y,TsuitI,TsuitII,Rsuit,totalRain,suitI,suitII,tmp\n')
		while count < len(record):
			r=record[count]
			suitI=(r['TsuitI']*r['Rsuit'])/100
			suitII=(r['TsuitII']*r['Rsuit'])/100
			file.write(str(r['#']-1)+','+str(r['X'])+','+str(r['Y'])+','+\
			str(r['TsuitI'])+','+str(r['TsuitII'])+','+\
			str(r['Rsuit'])+','+str(r['totalRain'])+','+\
			str(suitI)+','+str(suitII)+','+str(int(suitI))+'\n')
			count=count+1		

	with open(os.path.join(output, 'log.txt'), 'w+') as file:
		file.write('\tMt\n')
		for key, value in Mt.iteritems():
			file.write('<'+str(key)+'>: '+str(value)+'\n')
		file.write('\tAt\n')
		for key, value in At.iteritems():
			file.write('<'+str(key)+'>: '+str(value)+'\n')
	print 'totol record: '+str(len(record))

	
def Browse(E, SS):
	path=tkFileDialog.askdirectory()
	E.delete(0, END)
	E.insert(0, path)
	
	files=getFiles(path)
	print len(files)
	SS.set(' '+str(len(files))+' files in selected')


