#Zeke800's APT colorizer
from PIL import Image
import PIL.ImageOps
import sys

args = list(sys.argv)

try:
    args[1]
except:
    args.append("-noir")

#images
ch2 = Image.open("chb_4.png").convert("L")
ch4 = Image.open("cha_4.png").convert("L")

#ch4 = PIL.ImageOps.invert(ch4)
#ch4 = PIL.ImageOps.autocontrast(ch4)
ch2 = PIL.ImageOps.autocontrast(ch2)

#Variables
deyellowfactor = 100
black_pixels = []

#convert to arrays
ch2_array = ch2.load()
ch4_array = ch4.load()

#sizes
xsize,ysize = ch2.size

#output
outimg = Image.new('RGB',(xsize,ysize))
#main loop
if args[1] == "-ir":
    for y in range(ysize):
        for x in range(xsize):
            if ch2_array[x,y] - ch4_array[x,y] <= -50:
                outimg.putpixel((x,y),(ch4_array[x,y],ch4_array[x,y],int(1*ch4_array[x,y])))
            else:
                outimg.putpixel((x,y),(ch2_array[x,y],ch2_array[x,y],int(1*ch4_array[x,y])))
else:
    for y in range(ysize):
        for x in range(xsize):
            outimg.putpixel((x,y),(ch2_array[x,y],ch2_array[x,y],int(1*ch4_array[x,y])))

outimg = PIL.ImageOps.autocontrast(outimg)
outimg.save("color.png")
