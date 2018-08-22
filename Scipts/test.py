### Murat Goncu
# Script to detect license plates.

import numpy as np
import cv2
import argparse
import imutils


CASCADE_PATH = '/Users/muratgoncu/opencv/data/haarcascades/cascade.xml'
RESIZE_HEIGHT = 600

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image to be scanned")
args = vars(ap.parse_args())

# Initiate cascade classifer.
plate_cascade = cv2.CascadeClassifier(CASCADE_PATH)

# Get image from given path
img = cv2.imread(args["image"])

# Resize image 
img   = imutils.resize(img, height = RESIZE_HEIGHT)

# Filter image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect plates in img
plates = plate_cascade.detectMultiScale(gray,5,20)
    
print("Found %d plates:" %len(plates))
for (x,y,w,h) in plates:
	print x,y,w,h

	# Draw rectangle around found plates.
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


# Show image.
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()