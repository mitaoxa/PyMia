import draw_town as town
import Image

im=Image.new('RGBA', (5*200, 5*360))
town.DrawTown(im)

im.save('base_cut.png')
