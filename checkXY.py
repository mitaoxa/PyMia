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

print '===== X =====',str(len(X)),'\n',sorted(X)
print '===== Y =====',str(len(Y)),'\n',sorted(Y)
