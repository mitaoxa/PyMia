import os
import Image, ImageDraw
import tkFileDialog
import csv
from collections import namedtuple

path= tkFileDialog.askopenfilename()

unit, col, row=5, 200, 360
im=Image.new('RGBA', (unit*col, unit*row))
D=ImageDraw.Draw(im)

unit=unit*100
with open(path, 'r') as file:
	csvreader=csv.reader(file, delimiter=',')
	Header=next(csvreader)
	Data=namedtuple('Header', ','.join(Header))
	for row in csvreader:
		d = Data._make(row)
		distX, distY=0.001, 0.0001
		X, Y = float(d.X)-120.0, 25.47-float(d.Y)
		D.rectangle((X*unit, Y*unit, (X+distX)*unit, (Y+distY)*unit), fill='white')
		#print d.Z		
im.save("500m.png")
