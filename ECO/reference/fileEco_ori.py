import os
import tkFileDialog

path = tkFileDialog.askdirectory()
print 'path= '+path

names=[]

loc=[]
locations=[]
count=1
for root, dirnames, filenames in os.walk(path):
	for name in filenames:
		with open(os.path.join(path,name)) as file:
			lines = file.read().splitlines()
			tmp=lines[3].split()
			loc.append(str(count))
			loc.append(tmp[1])
			loc.append(tmp[2])
			locations.append(loc)
			loc=[]
			count=count+1
	break

output=os.path.join(path, 'output')
if not os.path.exists(output):
	os.makedirs(output)
with open(os.path.join(output, 'location.txt'), 'w+') as file:
	for loc in locations:
		file.write(' '.join(loc)+'\n')

print len(locations)


