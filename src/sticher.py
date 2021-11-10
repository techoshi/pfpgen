import sys
from PIL import Image
import argparse
from os import listdir
from os import path


async def stitch(output_dir, filename, img_args, x, y):
    newImage = Image.new('RGBA', (x, y))
    #name = "".join(choices(string.ascii_letters, k=5)) + "_"
    try:
        name = "_"
        for imagePath in img_args:
            if imagePath != None:
                basename = path.basename(imagePath)
                fname = path.splitext(basename)[0]
                name += str(fname) + "_"
                img = Image.open(imagePath)
                if img.mode == "RGB":
                    img = img.convert("RGBA")
                newImage.alpha_composite(img)
            else:
                name += str(None) + "_"

        if filename == "":
            filename = name
        newImage.save(output_dir + filename + ".png") 
        print("minted #" + filename)
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")              
        logFile1 = open(output_dir + 'failedStich.txt','a+')
        logFile1.write(filename + "\n")
        logFile1.close()  
    return True

    