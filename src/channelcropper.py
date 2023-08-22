from PIL import Image


# Constants
APT_SYNC_WIDTH = 39
APT_SPC_WIDTH = 47
APT_TELE_WIDTH = 45
APT_FRAME_LEN = 128
APT_CH_WIDTH = 909


def crop(image: Image, upper: int, lower: int, left: int, right: int) -> Image:
    return image.crop((left, upper, right, lower))
    

def divide(image: Image):
    xsize, ysize = image.size
    
    # Crop Channel A
    cha = crop(image, 1, ysize, APT_SYNC_WIDTH + APT_SPC_WIDTH, APT_SYNC_WIDTH + APT_SPC_WIDTH + APT_CH_WIDTH - 10)
    cha = cha.resize((APT_CH_WIDTH, ysize), Image.ANTIALIAS)
    
    # Cut channel B
    chb = crop(image, 1, ysize, APT_SYNC_WIDTH + APT_SPC_WIDTH + APT_CH_WIDTH + APT_SYNC_WIDTH + APT_SPC_WIDTH +
               APT_TELE_WIDTH, APT_SYNC_WIDTH + APT_SPC_WIDTH + APT_CH_WIDTH + APT_SYNC_WIDTH + APT_SPC_WIDTH +
               APT_TELE_WIDTH + APT_CH_WIDTH - 10)
    chb = chb.resize((APT_CH_WIDTH, ysize), Image.ANTIALIAS)
    
    cha.save('../out/cha.png')
    chb.save('../out/chb.png')
    
    return cha, chb
