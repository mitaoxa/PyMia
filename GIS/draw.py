import os
import Image, ImageDraw

def Create_draw(path,Dir):
	with open(path) as file:
		lines=file.read().splitlines()

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
	unit, row, col= 5, len(point), len(point[0].split()) #5, 360, 200
	print str(unit), str(row), str(col)

	im=Image.new('RGBA', (unit*col,unit*row))
	D=ImageDraw.Draw(im)

	black=point[0].split()

	X, Y=0,0

	colorRamp={'min':(39,117,121),1:(35,122,150),2:(48,135,162),3:(64,152,175),4:(81,158,186),5:(74,154,181),6:(102,183,200),7:(124,196,208),8:(135,202,219),9:(158,211,229),10:(159,223,235),11:(179,239,247),12:(18,144,80),13:(23,146,79),14:(50,157,85),15:(62,168,96),16:(79,172,102),17:(102,183,116),18:(125,192,121),19:(132,201,118),20:(147,212,130),21:(165,219,131),22:(186,226,137),23:(199,233,139),24:(211,238,145),25:(245,242,189),26:(242,233,140),27:(250,211,132),28:(242,197,94),29:(239,179,69),30:(230,159,53),31:(233,134,41),32:(234,120,8),33:(223,82,39),34:(235,19,92),35:(176,5,50),36:(114,6,0),37:(163,107,152),38:(132,82,153),'max':(125,35,159)}

	for key,value in point.iteritems():
		ps=value.split()
		for p in ps:
			if p == black[0]:
				X=X+unit
				continue
			temp=int(round(float(p)))
			if temp<0:
				color=colorRamp['min']
			elif temp>=38:
				color=colorRamp['max']
			else:
				color=colorRamp[temp+1]
			D.rectangle((X,Y,X+unit,Y+unit), fill=color)
			X=X+unit
		Y=Y+unit
		X=0

	filename=path[len(path)-27:len(path)-12]+'.png'
	print 'Dir: ', Dir	
	save=os.path.join(Dir, filename)
	print 'output: ',save
	im.save(save)
