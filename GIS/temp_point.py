import tkFileDialog
import os
import shapefile as shp

path= tkFileDialog.askopenfilename()

print 'path: <',path,'>'

with open(path) as file:
	lines=file.read().splitlines()

LONG, LAT=120.0, 25.4

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

w=shp.Writer(shp.POINT)
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
			w.point(LONG, LAT)
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
	
