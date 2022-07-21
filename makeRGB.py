#Zeke800's APT colorizer
#Convert APT images to color (224 composition)
from PIL import Image
import PIL.ImageOps
import sys

args = list(sys.argv)

try:
    args[1]
except:
    args.append("-noir")

try:
    args[2]    

except:
    if args[1] == "-boost":
        args.append("-boost")
    else:
        args.append("-noboost")

#images
ch2 = Image.open("cha.png").convert("L")
ch4 = Image.open("chb.png").convert("L")

#ch4 = PIL.ImageOps.invert(ch4)
#ch4 = PIL.ImageOps.autocontrast(ch4)
ch2 = PIL.ImageOps.autocontrast(ch2)

#Variables
deyellowfactor = 100
black_pixels = []
ch2_blend = 1
ch4_blend = 200
ch2_boost = 1.5
ch4_boost = 0.5

#convert to arrays
ch2_array = ch2.load()
ch4_array = ch4.load()

#sizes
xsize,ysize = ch2.size

#output
outimg = Image.new('RGB',(xsize,ysize))

def change_contrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast(c):
        return 128 + factor * (c - 128)
    return img.point(contrast)

#main loop
"""
for y in range(ysize):
    for x in range(xsize):
        
        ch4.putpixel((x,y),(ch2_array[x,y],ch2_array[x,y],int(1*ch4_array[x,y])))
"""
if args[1] == "-ir":
    for y in range(ysize):
        for x in range(xsize):
            if ch2_array[x,y] - ch4_array[x,y] <= -50:
                outimg.putpixel((x,y),(ch4_array[x,y],ch4_array[x,y],int(1*ch4_array[x,y])))
            else:
                outimg.putpixel((x,y),(ch2_array[x,y],ch2_array[x,y],int(1*ch4_array[x,y])))
elif args[1] == "-ir_night":
    for y in range(ysize):
        for x in range(xsize):
            if ch2_array[x,y] - ch4_array[x,y] <= -40:
                outimg.putpixel((x,y),(round(ch2_array[x,y]*0.8 + ch4_array[x,y]*0.2),round(ch2_array[x,y]*0.8 + ch4_array[x,y]*0.2),round(ch2_array[x,y]*0.8 + ch4_array[x,y]*0.2)))
                #black_pixels.append([x,y])
            else:
                    outimg.putpixel((x,y),(ch2_array[x,y],ch2_array[x,y],int(1*ch4_array[x,y])))

elif args[1] == "-sunset":
    for y in range(ysize):
        for x in range(xsize):
            if ch2_array[x,y] - ch4_array[x,y] <= -40:
                outimg.putpixel((x,y),(round(ch2_array[x,y]*ch2_blend),round(ch2_array[x,y]*ch2_blend),round(ch4_array[x,y]*ch2_array[x,y]/ch4_blend)))
                #black_pixels.append([x,y])
            else:
                    outimg.putpixel((x,y),(ch2_array[x,y],ch2_array[x,y],int(1*ch4_array[x,y])))

else:
    for y in range(ysize):
        for x in range(xsize):
            outimg.putpixel((x,y),(ch2_array[x,y],ch2_array[x,y],int(1*ch4_array[x,y])))
if args[2] == "-boost":
    outimg_array = outimg.load()
    for y in range(ysize):
        for x in range(xsize):
            outimg.putpixel((x,y),(round(outimg_array[x,y][0]*ch2_boost),round(outimg_array[x,y][1]*ch2_boost),round(outimg_array[x,y][2]*ch4_boost)))
            

outimg = PIL.ImageOps.autocontrast(outimg)
#outimg = change_contrast(outimg,100)

outimg.show()
outimg.save("color.png")
