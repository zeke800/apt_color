#!/usr/bin/env python3

import argparse

from array import array
from PIL import Image, ImageOps


# Constants
DEYELLOW_FACTOR = 100
CH2_BLEND = 1
CH4_BLEND = 200
CH2_BOOST = 1.5
CH4_BOOST = 0.5


def parse_args() -> dict:
    parser = argparse.ArgumentParser(description='NOAA APT Colorizer CLI', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-m', '--mode', type=str, default='noir', help='The mode, can be "ir", "ir_night", or "sunset"')
    parser.add_argument('-b', '--boost', action='store_true', help='Boost the land color on very blue images')
    parser.add_argument('cha', help='Source of channel A')
    parser.add_argument('chb', help='Source of channel B')
    args = parser.parse_args()

    return vars(args)


def get_images_arrays(arguments: dict) -> [array, array]:
    ch2 = Image.open(arguments['cha']).convert('L')
    ch2 = ImageOps.autocontrast(ch2)
    ch2_array = ch2.load()

    ch4 = Image.open(arguments['chb']).convert('L')
    ch4_array = ch4.load()

    return ch2.size, ch2_array, ch4_array


def colour(ch2_array: array, ch4_array: array, size: tuple, arguments: dict) -> Image:
    xsize, ysize = size
    outimg = Image.new('RGB', (xsize, ysize))

    match arguments['mode']:
        case 'ir':
            for y in range(ysize):
                for x in range(xsize):
                    if (ch2_array[x, y] - ch4_array[x, y]) <= -50:
                        outimg.putpixel((x, y), (ch4_array[x, y], ch4_array[x, y], int(1 * ch4_array[x, y])))
                    else:
                        outimg.putpixel((x, y), (ch2_array[x, y], ch2_array[x, y], int(1 * ch4_array[x, y])))
        case 'ir_night':
            for y in range(ysize):
                for x in range(xsize):
                    if (ch2_array[x,y] - ch4_array[x,y]) <= -40:
                        outimg.putpixel((x, y), (round(ch2_array[x, y] * 0.8 + ch4_array[x,y] * 0.2),
                                                 round(ch2_array[x,y] * 0.8 + ch4_array[x,y] * 0.2),
                                                 round(ch2_array[x,y] * 0.8 + ch4_array[x,y] * 0.2)))
                    else:
                        outimg.putpixel((x, y), (ch2_array[x, y], ch2_array[x, y], int(1 * ch4_array[x, y])))
        case 'sunset':
            for y in range(ysize):
                for x in range(xsize):
                    if (ch2_array[x,y] - ch4_array[x,y]) <= -40:
                        outimg.putpixel((x, y), (round(ch2_array[x, y] * CH2_BLEND),
                                                 round(ch2_array[x, y] * CH2_BLEND),
                                                 round(ch4_array[x, y] * ch2_array[x, y] / CH4_BLEND)))
                    else:
                        outimg.putpixel((x, y), (ch2_array[x, y], ch2_array[x, y], int(1 * ch4_array[x, y])))
        case 'noir':
            for y in range(ysize):
                for x in range(xsize):
                    outimg.putpixel((x, y), (ch2_array[x, y], ch2_array[x, y], int(1 * ch4_array[x, y])))
        case _:
            raise Exception('Modes supported are "ir", "ir_night", and "sunset"')

    return outimg


def boost(image: Image, size: array, arguments: dict) -> Image:
    if arguments['boost']:
        xsize, ysize = size
        outimg_array = image.load()

        for y in range(ysize):
            for x in range(xsize):
                image.putpixel((x, y), (round(outimg_array[x, y][0] * CH2_BOOST),
                                        round(outimg_array[x, y][1] * CH2_BOOST),
                                        round(outimg_array[x, y][2] * CH4_BOOST)))
    
    return image


def export_image(image: Image):
    out_image = ImageOps.autocontrast(image)

    out_image.show()
    out_image.save('color.png')


if __name__ == '__main__':
    args: dict = parse_args()
    size, ch2, ch4 = get_images_arrays(args)
    image = colour(ch2, ch4, size, args)
    image = boost(image, size, args)

    export_image(image)
