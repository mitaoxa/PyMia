import shapefile
import Image, ImageDraw


def DrawDetail(points, D, unit):
        pre, first = None, None
        for p in points:
                if pre == None:
                        pre = [p[0]-120.0, 25.47-p[1]]
                        first = pre
                else:
                        p = [p[0]-120.0, 25.47-p[1]]
                        D.line((pre[0]*unit, pre[1]*unit, p[0]*unit, p[1]*unit), fill='black', width=1)
                        pre = p
def DrawTown(im):
        sf=shapefile.Reader("town/Town_MOI_1041215.shp")
        shapes=sf.shapes()

        unit, col, row=5, 200, 360
        #im=Image.new('RGBA', (unit*col, unit*row))
        D=ImageDraw.Draw(im)
        unit=unit*100
        for shape in shapes:
                points=shape.points
                pre = None
                start = False
                if len(shape.parts) >1:
                        for p in shape.parts:
                                if not start:
                                        start = True
                                else:
                                        DrawDetail(points[pre:p], D, unit)
                                pre = p
                else:
                        DrawDetail(points, D, unit)
def MaskTown(im):
	base=Image.open('result.png')
	im.paste(base, (0,0), base)
