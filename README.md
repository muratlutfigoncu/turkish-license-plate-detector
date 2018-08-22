# License Plate Detector

This repository contains the codes, samples images and tutorial necessary to train a haar cascade using Python and OpenCV to detect turkish and european union license plates. 


1 - Gather pos images put in positive_images folder
For EU license plates you can find positive image dataset in openalpr repository: 
https://github.com/openalpr/train-detector/tree/master/eu

2 - Gather neg images put in negative_.
You can also find negatives images in the same repository.


3 - Resize positive images to 200x200. We can use imagemagick tool to resize our images. Used a script to resize all images in a folder:

```bash

for i in *.JPG; do
    printf "Resize $i\n"
    convert "$i" -resize 200x200 "$i"
done

```

4 - Now let's create a text file containing all the negative image names.

```bash
find ./negative_images -iname "*.jpg" > negatives.txt
```
5 - In the same way create a text file for positive images

```bash
find ./positive_images -iname "*.jpg" > positives.txt
```

5 - Run sample creator script. This script will create 10 samples for each positive image. Change the positive image folder path and negative text file path and the number of sample to be created


6 - Create vec file: 
```bash
opencv_createsamples -info info/info.lst -num 4000 -w 52 -h 13 -vec positives.vec
```

7 - Let's start training. Use less pictures in training than created samples: 4000 -> 3800. And also try to keep positive/negative images ratio to 2:1.
```bash
opencv_traincascade -data data -vec positives.vec -bg negatives.txt -numPos 3800 -numNeg 1900 -numStages 10 -w 52 -h 13

### If you want to run training in background;
nohup opencv_traincascade -data data -vec positives.vec -bg negatives.txt -numPos 3800 -numNeg 1900 -numStages 10 -w 52 -h 13 &
```

In my mac the last step took about 7 hours. (Processor: i5, Memory: 8 GB)

8 - After the training, you will see a cascade file under data. Let's test our trained cascade using test.py. But first change the cascade file path in test.py and then run commnand:

```bash
 python test.py --image [IMAGE_PATH]
```

9 - Output

![alt text](https://raw.githubusercontent.com/muratlutfigoncu/turkish-license-plate-detector/master/output/output.png)

The output is not great but still works. Will try to rerun training after collecting more images.


# Features to be added

- Reading license plate number using Tesseract
- Capturing license plates in videos