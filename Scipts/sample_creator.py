### create samples using opencv

import os
import time


## Change these values.
IMAGE_FOLDER = "FOLDER_NAME"
NEGATIVES = "negatives.txt"
SAMPLE_NUM = "10"

for filename in os.listdir(IMAGE_FOLDER):

    command = "opencv_createsamples -img positive_images/" + filename + " -bg " + NEGATIVES + " -info info/info-temp.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num " + SAMPLE_NUM
    os.system(command)
    time.sleep(0.2)
    f = open("info/info-temp.lst", "r")
    content = f.read()
    file = open("info/info.lst", "a")
    file.write(content)
