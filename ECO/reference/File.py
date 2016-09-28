import os
import tkFileDialog

pin = tkFileDialog.askdirectory()
print 'path= '+pin

loc=[]
locations=[]

for root, dirnames, filenames in os.walk(pin):
	for name in filenames:
		with open(os.path.join(pin, name)) as file:
			lines = file.read().splitlines()
			print lines[3]

