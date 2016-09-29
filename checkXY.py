import tkFileDialog
import os


Dir=tkFileDialog.askdirectory()

for root, dirname, filename in os.walk(Dir):
	files=filename
	break
X, Y=[],[]
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

print '===== X ====='#,str(len(X)),'\n',X,'\n',sorted(X)

nX, preX=1, 0
disX, disY=[],[]
count=0
for x in sorted(X):
	n=int(round(1000*(float(x)-preX)))
	if not n == nX and not preX == 0:
		count=count+1
		if not n in disX:
			disX.append(n)
			print n
	preX=float(x)

print 'total: ',str(count),'/',len(X)

#print '===== Y =====',str(len(Y)),'\n',sorted(Y)
