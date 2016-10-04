import os
import shapefile as shp


def Create_shp(path, Dir):
	with open(path) as file:
		    lines=file.read().splitlines()

	LONG, LAT=120.0, 25.47

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

	w=shp.Writer(shp.POLYGON)
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
		                    #left up -> right up -> right down -> left down
		                    loc=[LONG, LAT]
		                    LU=[LONG-0.005, LAT+0.005]
		                    RU=[LONG+0.005, LAT+0.005]
		                    RD=[LONG+0.005, LAT-0.005]
		                    LD=[LONG-0.005, LAT-0.005]
		                    par=[LU, RU, RD, LD, LU]
		                    w.poly(parts=[par])
		                    w.record(count, LONG, LAT, p)
	#               w.point(LONG, LAT)
	#               w.record(count, LONG, LAT, p)
		            count=count+1
		            LONG=LONG+0.01
		    LAT=LAT-0.01
		    LONG=120.0

	filename=path[len(path)-27:len(path)-12]
	d=os.path.join(Dir, filename)
	if not os.path.exists(d):
		os.makedirs(d)
	path_shp=os.path.join(d,filename+'.shp')
	w.save(path_shp)

	print 'output file ',path_shp

