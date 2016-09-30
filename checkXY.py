import tkFileDialog
import os


Dir=tkFileDialog.askdirectory()

for root, dirname, filename in os.walk(Dir):
	files=filename
	break
X, Y=[],[]
wXY={}
for f in files:
	with open(os.path.join(Dir,f)) as file:
		lines=file.read().splitlines()
		detail=lines[3].split()
		x=detail[2]
		y=detail[1]
		if not x in X:
			X.append(x)
		if not y in Y:
			Y.append(y)
		wXY[f[:4]]=x+' '+y

print '===== X ====='#,str(len(X)),'\n',X,'\n',sorted(X)

nX, preX=1, 0
disX, disY={},{}
count=0
Xs=[]
for x in sorted(X):
	n=int(round(1000*(float(x)-preX)))
	if not n == nX and not preX == 0:
		if disX.has_key(n):
			disX[n]=disX[n]+1
		else:
			disX[n]=1
	preX=float(x)
	if not x in Xs:
		Xs.append(x)

for key,value in  sorted(disX.iteritems(), key=lambda (k,v):(v,k)):
	print key,': ',value

X=sorted(X)
print 'X: <', X[0],'>, <', X[len(X)-1],'> / ',str(len(X))
print 'Xs: ', str(len(Xs))
print wXY

with open(os.path.join(Dir,'XY.txt'),'w+') as file:
	for index, value in wXY.iteritems():
		file.write(index+' '+value+'\n')



#print '===== Y =====',str(len(Y)),'\n',sorted(Y)
