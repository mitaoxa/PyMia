w = shapefile.Writer(shapefile.POLYGON)
w.field('name','C',50)
with open('your.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        bl  = [float(row['xl']),float(row['yb'])]
        tl  = [float(row['xl']),float(row['yt'])]
        br  = [float(row['xr']),float(row['yb'])]
        tr  = [float(row['xr']),float(row['yt'])]
        parr = [tl, tr, br, bl, tl]
        w.poly(parts=[parr])
        w.record(row['name'])

w.save("your.shp')
