from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

def rndStr():
	str=''
	chars= 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
	length=len(chars)-1
	return chars[(random.randint(0,length))]

def rndColor():
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def rndColor2():
	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width = 60 * 4
height = 60
im=Image.new('RGB',(width,height),(255,255,255))



font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf',36)

draw = ImageDraw.Draw(im)

for x in range(width):
	for y in range(height):
		draw.point((x,y),fill=rndColor())


for t in range(4):
	draw.text((60*t + 10, 10), rndStr(), font=font, fill=rndColor2())

im.filter(ImageFilter.GaussianBlur(0.5)).show()

#im.save('code.jpg')


