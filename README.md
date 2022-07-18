# apt_color
Turn APT images into HRPT-like composites. No overlays like WXtoIMG, no weird underlays, or requiring where the satellite was when the image was taken. As an example to the power of this tool, take a look at this:

![image](https://user-images.githubusercontent.com/82127189/179418072-c21e5786-f5de-4c92-8d04-6766579eb985.png)

Neat, huh? Anyways, here's how to use it :)

# Motivation

After seeing too many black and white ugly images. Moving on.

# Get. Rid. Of. The. Yellow. Tinge.

Coming soon! It is quite complex, though, so it may take a while. While you wait, get an HRPT setup.

## Why does it happen, though?

Essentially, the visible channel gets too bright. When making an HRPT composite, standard 221 is used, and the channel 2 increases along with the channel 1. But on APT, there is no channel 1, so channel 4 is used, however, it becomes ugly in terms of brightness. Essentially, a good idea is to try to get NOAA-18 APT, or try not to get too much varying brightness in channel 2. 


# How to run it

MakeRGB.py takes in two arguments - cha.png, chb.png, output.png. (Note that if you are using the BETA version you also need to specify the -y flag to remove yellow or not.) To generate seperate channels from APT images, use the channelseperate.py script (input.png, cha.png, chb.png)!


