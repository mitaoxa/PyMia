import os
import tkFileDialog

startX, startY=120038, 252878
pX, pY=40, 76 #count of row, column
nX, nY=49, 451
mapX, mapY={}, {}

def getX(mapX, x):
	if not mapX.has_key(x):
		for key in sorted(mapX):
			if round(int(abs(x-mapX[key]))) < 20:
#				print '\t', x,'> ',key
				return mapX[key]
		print 'error: ',x,'>',key
	else:
		return mapX[x]
def getY(mapY, y):
	if not mapY.has_key(y):
		for key in sorted(mapY):
			if round(int(abs(y-mapY[key]))) < 220:
				return mapY[key]
		print 'error: ', y,'>',key
	else:
		print 'why being here?'
		return mapY[y]

for i in range(pX):
	x=startX+nX*i
	if not mapX.has_key(x):
		mapX[x]=x

for i in range(pY):
	y=startY-nY*i
	if not mapY.has_key(y):
		mapY[y]=y

path=tkFileDialog.askopenfilename()
print path
with open(path, 'r') as file:
	lines=file.read().splitlines()
	for line in lines:
		detail=line.split()
		x=int(round(float(detail[1])*1000))
		y=int(round(float(detail[2])*10000))
		if not mapX.has_key(x):
			mapX[x]=getX(mapX, x)
		if not mapY.has_key(y):
			mapY[y]=getY(mapY, y)

disX, disY=[],[]
for key, value in mapX.iteritems():
	if not value in disX:
		disX.append(value)

for key, value in mapY.iteritems():
	if not value in disY:
		disY.append(value)

print 'total X= ',str(len(disX))
print 'total y= ',str(len(disY))

with open('mapX.txt','w+') as file:
	for key, value in mapX.iteritems():
		file.write(str(key)+' '+str(value)+'\n')
with open('mapY.txt','w+') as file:
	for key, value in mapY.iteritems():
		file.write(str(key)+' '+str(value)+'\n')

#print sorted(mapX)

