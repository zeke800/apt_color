# apt_color
Turn APT images into HRPT-like composites. No overlays like WXtoIMG, no weird underlays, or requiring where the satellite was when the image was taken. As an example to the power of this tool, take a look at this:

![apt_color_header](https://user-images.githubusercontent.com/82127189/180015172-bf8c05be-162d-44b2-a38c-67b5dfaab296.png)


Neat, huh? Anyways, here's how to use it :)

# Motivation

After seeing too many black and white ugly images. Moving on.

# Get. Rid. Of. The. Yellow. Tinge.

Coming soon! It is quite complex, though, so it may take a while. While you wait, get an HRPT setup.

## Why does it happen, though?

Essentially, the visible channel gets too bright. When making an HRPT composite, standard 221 is used, and the channel 2 increases along with the channel 1. But on APT, there is no channel 1, so channel 4 is used, however, it becomes ugly in terms of brightness. Essentially, a good idea is to try to get NOAA-18 APT, or try not to get too much varying brightness in channel 2. 


# How to run it

MakeRGB.py takes in one argument -ir (used to do ir blend on a sunset scene). It looks for two images called cha.png and chb.png. Color images are saved in color.png. To generate seperate channels from APT images, use the channelseperate.py script (input.png, cha.png, chb.png)! Note that the images are actually **almost** the same size but still need to be resized seperately. Work in progress.

# Image Gallery
![image](https://user-images.githubusercontent.com/82127189/179874305-f79dab5b-1c4c-4227-b4fd-fd2273783c05.png)
![image](https://user-images.githubusercontent.com/82127189/179874347-7ae5fa79-27be-4935-b0d9-2ff2352627f0.png)
![image](https://user-images.githubusercontent.com/82127189/179874370-1a154e36-0a6a-4f34-9ae1-92bbd588d747.png)
![image](https://user-images.githubusercontent.com/82127189/179874382-27db0415-18b0-437b-847d-633d82fd50d4.png)



