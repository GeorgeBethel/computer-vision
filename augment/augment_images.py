import argparse
import os
import cv2
import numpy as np

ap = argparse.ArgumentParser()

ap.add_argument("-i", --input, required=True,
	help="path to image")

ap.add_argument("-o", "--output", required=True,
	help="path to save image")

ap.add_argument("-r", "--rotation", required=True,
	help="to rotate image")

ap.add_argument("-z", "--zoom", required=True,
	help="to zoom image")

ap.add_argument("-g", "--gray_scale", required=True,
	help="to convert to gray scale")

args = vars(ap.parse_args())

num_dir_image = len(args["input"])  # to geth the number of images in the path
list_of_files=list() #list to hold the images in the path
list_of_images = os.listdir(args["input"]) #stores the list of images in a list

#print(os.listdir(os.getcwd()))

def rotate_image(index,img):
    image = cv2.imread(img)
    rows,cols = image.shape[:2]
    angle = 30
    zoom =2.5
    M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,zoom) 
    rotated_image = cv2.warpAffine(image,M,(cols,rows))
    cv2.imwrite(os.path.join(args["output"],list_of_images[index]),rotated_image)


for index,image in enumerate(list_of_images):
    img = os.path.join(args["input"],image)
    print(img)
    #img = cv2.imread(img)
    if args["rotation"] == "True":
        rotate_image(index,img)
        print("reached here")
        #cv2.imwrite(f'aug_image_{angle}.jpg',augumented_image,[cv2.IMWRITE_JPEG_QUALITY,100]
    else:
        pass
    
print("done augmenting")        

    

    
#image = cv2.imread('james.jpg')



