#!/usr/bin/env python3

from PIL import Image, ImageFilter

import os

#size_300=(300,300)
#size_700=(700,700)
image1=Image.open('figure_1.jpg')

#image1.rotate(90).show()
##https://pillow.readthedocs.io/en/4.0.x/handbook/concepts.html#concept-modes
#image1.convert(mode='L').save('figure_2.jpg')
##https://pillow.readthedocs.io/en/4.0.x/reference/ImageFilter.html#module-PIL.ImageFilter
image1.filter(ImageFilter.GaussianBlur(1)).show()

#for i in os.listdir('.'):
#    if i.endswith('.jpg'):
#        file,file_ext=os.path.splitext(i)
#        P=Image.open(i)
#        P.thumbnail(size_300)
#        P.save('300/%s_300.%s' % (file,file_ext))
#        P.thumbnail(size_700)
#        P.save('700/%s_700.%s' % (file,file_ext))       