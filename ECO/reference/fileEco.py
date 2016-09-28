import os
import tkFileDialog

path = tkFileDialog.askdirectory()
print 'path= '+path

names=[]

loc=[]
locations={}
#count=0
for root, dirnames, filenames in os.walk(path):
	#print filenames
	for name in filenames:
		#print int(name[:4])
		index=int(name[:4])
		with open(os.path.join(path,name)) as file:
			lines = file.read().splitlines()
			tmp=lines[3].split()
			#loc.append(str(count))
			loc.insert(1,tmp[1])
			loc.insert(0,tmp[2])
#			locations.insert((index-1), loc)
			locations[index-1]=loc
			loc=[]
			#count=count+1
	break

output=os.path.join(path, 'output')
if not os.path.exists(output):
	os.makedirs(output)
count=0
with open(os.path.join(output, 'location.txt'), 'w+') as file:
	file.write('FID X Y\n')
	while count < len(locations):
		loc=locations[count]
		file.write(str(count)+' '+str(loc[0])+' '+str(loc[1])+' '+'\n')
		count = count+1
#	for loc in locations:
#		file.write(' '.join(loc)+'\n')

print len(locations)


