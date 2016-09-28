import csv
import tkFileDialog
import shapefile


path=tkFileDialog.askopenfilename()

Name, Part=[], []

with open(path, 'rb') as f:
	reader = csv.DictReader(f)
	for row in reader:
		print row
		bl = [float(row['xl']), float(row['yb'])]
		tl = [float(row['xl']), float(row['yt'])]
		br = [float(row['xr']), float(row['yb'])]
		tr = [float(row['xr']), float(row['yt'])]
		par=[tl, tr, br, bl, tl]
		Name.append(row['name'])
		Part.append(par)
w=shapefile.Writer(shapefile.POLYGON)
w.field('name','C', 50)

for part, name in zip(Part, Name):
	w.poly(parts=[part])
	w.record(name)

w.save('output.shp')
		
