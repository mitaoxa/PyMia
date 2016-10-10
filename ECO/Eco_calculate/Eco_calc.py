from Tkinter import *
import Tkinter as tk
import ttk as ttk
import os
import tkFileDialog
import shapefile as shp
import csv
from collections import namedtuple
import Image, ImageDraw
import mapXY

def getZ():
#	pZ=tkFileDialog.askopenfilename()
	pZ='output_Z.txt'
	with open(pZ, 'r') as fin:
		csvreader=csv.reader(fin, delimiter=',')
		Header=next(csvreader)
		Data=namedtuple('Header', ','.join(Header))
		Z={}
		for row in csvreader:
			d = Data._make(row)
			Z[int(float(d.ID)-1)]=float(d.Z)
	return Z

def DrawPic(nl, na, unit, colorRamp, record, lmin, amax, path, i):
        im=Image.new('RGBA', (unit*nl,unit*na))
        D=ImageDraw.Draw(im)

        for key, r in record.iteritems():
		if i=='I':
			suit=int((r['TsuitI']*r['Rsuit'])/1000)
		elif i=='II':
                	suit=int((r['TsuitII']*r['Rsuit'])/1000)
		elif i=='R':
			suit=int(r['totalRain']/1000)
			if suit >=5:
				suit=5
		elif i=='TAV':
			suit=int(round(float(r['TAV'])/10))
                if suit == 0:
                        color=colorRamp[0]
                else:
                        color=colorRamp[suit]
                X=int(round((float(r['X'])-lmin)/0.049))
                Y=int(round((amax-float(r['Y']))/0.045))

                D.rectangle((X*unit,Y*unit,(X+1)*unit, (Y+1)*unit),fill=color)
	im.save(path)
	print 'path: ',path

def getPoint(path, record, SS):
	output=os.path.join(path, 'shapefile')
	if not os.path.exists(output):
		os.makedirs(output)	
	Z=getZ()

	w=shp.Writer(shp.POINT)
	w.autoBalance=1
	w.field('ID', 'N')
	w.field('X', 'F', 10, 8)
	w.field('Y', 'F', 10, 8)
	w.field('suitI', 'F', 10, 8)
	w.field('suitII', 'F', 10, 8)
	w.field('Rsuit', 'F', 10, 8)
	w.field('TAV', 'F', 10, 8)
	w.field('totalR', 'F', 10, 8)

	count=0
	for key, r in record.iteritems():
		if Z[key] >=500:
			suitI=0
			suitII=0
			count=count+1
		else:
			suitI=(r['TsuitI']*r['Rsuit'])/100
			suitII=(r['TsuitII']*r['Rsuit'])/100
		X=r['X']
		Y=r['Y']
		w.point(X, Y)
		w.record((r['#']-1), X, Y, suitI, suitII, r['Rsuit'], r['TAV'], r['totalRain'])

	filename=path[len(path)-4:]+'_point.shp'
	shpfile=os.path.join(output, filename)
	
	SS.set('file: '+shpfile)
	w.save(shpfile)
	print 'shapfile output success: ',shpfile

def getShp(path, record, SS):
	output=os.path.join(path, 'shapefile')
	if not os.path.exists(output):
		os.makedirs(output)	
	Z=getZ()

	w=shp.Writer(shp.POLYGON)
	w.autoBalance=1
	w.field('ID', 'N')
	w.field('X', 'F', 10, 8)
	w.field('Y', 'F', 10, 8)
	w.field('suitI', 'F', 10, 8)
	w.field('suitII', 'F', 10, 8)
	w.field('Rsuit', 'F', 10, 8)
	w.field('TAV', 'F', 10, 8)
	w.field('totalR', 'F', 10, 8)

	count=0
	for key, r in record.iteritems():
		if Z[key] >=500:
			suitI=0
			suitII=0
			count=count+1
		else:
			suitI=(r['TsuitI']*r['Rsuit'])/100
			suitII=(r['TsuitII']*r['Rsuit'])/100
		X=r['X']
		Y=r['Y']
		LU=[X-0.025, Y+0.023]
		RU=[X+0.025, Y+0.023]
		RD=[X+0.025, Y-0.023]
		LD=[X-0.025, Y-0.023]
		par=[LU, RU, RD, LD, LU]
		w.poly(parts=[par])
		w.record((r['#']-1), X, Y, suitI, suitII, r['Rsuit'], r['TAV'], r['totalRain'])

	filename=path[len(path)-4:]+'_grid.shp'
	shpfile=os.path.join(output, filename)
	
	SS.set('file: '+shpfile)
	w.save(shpfile)
	print 'shapfile output success: ',shpfile

def getPic(path, record, SS):
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
        colorRamp={10:(62,168,96),9:(79,172,102),8:(102,183,116),7:(125,192,121),6:(132,201,118),5:(147,212,130),4:(165,219,131),3:(186,226,137),2:(199,233,139),1:(211,238,145),0:(245,242,189)}
	TAVcolorRamp={'min':(39,117,121),1:(35,122,150),2:(48,135,162),3:(64,152,175),4:(81,158,186),5:(74,154,181),6:(102,183,200),7:(124,196,208),8:(135,202,219),9:(158,211,229),10:(159,223,235),11:(179,239,247),12:(18,144,80),13:(23,146,79),14:(50,157,85),15:(62,168,96),16:(79,172,102),17:(102,183,116),18:(125,192,121),19:(132,201,118),20:(147,212,130),21:(165,219,131),22:(186,226,137),23:(199,233,139),24:(211,238,145),25:(245,242,189),26:(242,233,140),27:(250,211,132),28:(242,197,94),29:(239,179,69),30:(230,159,53),31:(233,134,41),32:(234,120,8),33:(223,82,39),34:(235,19,92),35:(176,5,50),36:(114,6,0),37:(163,107,152),38:(132,82,153),'max':(125,35,159)}
	RcolorRamp={0:(194,82,60),1:(237,168,19),2:(198,247,0),3:(14,196,65),4:(22,109,138),5:(12,47,122)}

	filenameI=path[len(path)-4:]+'_suitI.png'
	pathI=os.path.join(pic, filenameI)
	filenameII=path[len(path)-4:]+'_suitII.png'
	pathII=os.path.join(pic, filenameII)
	filenameR=path[len(path)-4:]+'_suitR.png'
	pathR=os.path.join(pic, filenameR)
	filenameTAV=path[len(path)-4:]+'_TAV.png'
	pathTAV=os.path.join(pic, filenameTAV)
	DrawPic(nl, na, unit, colorRamp, record, lmin, amax, pathI, 'I')
	DrawPic(nl, na, unit, colorRamp, record, lmin, amax, pathII, 'II')
	DrawPic(nl, na, unit, RcolorRamp, record, lmin, amax, pathR, 'R')
	DrawPic(nl, na, unit, colorRamp, record, lmin, amax, pathTAV, 'TAV')

	
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
	suit['X']=mapXY.mapX[float(detail[2])*1000]/1000.0
	suit['Y']=mapXY.mapY[int(round(float(detail[1])*10000))]/10000.0
	TAV=float(detail[4])
#	suit['location']=location
	count=5
	for line in lines[5:]:
		tmp=line.split()
		meanT.append((float(tmp[2])+float(tmp[3]))/2)
		Rain.append(float(tmp[4]))
		count=count+1
	count=0
	if TAV >= E['Topmin'] and TAV <= E['Topmax']:
		suit['TAV']=100
	elif TAV < E['Tmin'] or TAV > E['Tmax']:
		suit['TAV']=0
	elif TAV < E['Topmin'] and TAV >= E['Tmin']:
		suit['TAV']=At['TLess']+Mt['TLess']*TAV
	elif TAV > E['Topmax'] and TAV <= E['Tmax']:
		suit['TAV']=At['TMore']+Mt['TMore']*TAV
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
	print 'temp'
	print 'calc_ end, output shapfile'
	#########################################################
	#			calc_ end			#
	#########################################################
	getPic(path, record, SS)
	getShp(path, record, SS)
	getPoint(path, record, SS)

"""
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

	"""
def Browse(E, SS):
	path=tkFileDialog.askdirectory()
	E.delete(0, END)
	E.insert(0, path)
	
	print str(len(mapXY.mapX)),'/',str(len(mapXY.mapY))
	


