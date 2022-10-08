from PIL import Image
import sys
#These were shamelessly taken from aptdec
APT_SYNC_WIDTH = 39
APT_SPC_WIDTH = 47
APT_TELE_WIDTH = 45
APT_FRAME_LEN = 128
APT_CH_WIDTH = 909

i = Image.open(sys.argv[1]).convert("L")
iar = i.load()
xsize,ysize = i.size
cha = Image.new('RGB',(APT_CH_WIDTH,ysize))
chb = Image.new('RGB',(APT_CH_WIDTH,ysize))

(left, upper, right, lower) = (
        APT_SYNC_WIDTH + APT_SPC_WIDTH,
        1,
        APT_SYNC_WIDTH + APT_SPC_WIDTH + APT_CH_WIDTH - 10,
        ysize
    )
cha = i.crop((left, upper, right, lower))

#cha.show()
(left, upper, right, lower) = (
        APT_SYNC_WIDTH + APT_SPC_WIDTH + APT_CH_WIDTH + APT_SYNC_WIDTH + APT_SPC_WIDTH + APT_TELE_WIDTH,
        1,
        APT_SYNC_WIDTH + APT_SPC_WIDTH + APT_CH_WIDTH + APT_SYNC_WIDTH + APT_SPC_WIDTH + APT_TELE_WIDTH + APT_CH_WIDTH - 10,
        ysize
    )

chb = i.crop((left, upper, right, lower))

#chb.show()

cha = cha.resize((APT_CH_WIDTH,ysize), Image.ANTIALIAS)
chb = chb.resize((APT_CH_WIDTH,ysize), Image.ANTIALIAS)

cha.save(sys.argv[2])
chb.save(sys.argv[3])
