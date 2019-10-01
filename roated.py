import argparse
import imutiles
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("--image", required=True, help="enter Path to the image")
args = vars(ap.parse_args())

image_name = args["image"]

if os.path.isfile(image_name):
    print(f'Using file {image_name}')
else:
    raise FileNotFoundError(image_name)

image = cv2.imread(image_name)
cv2.imshow("original image", image)


resized = imutiles.resize(image, width=100)
cv2.imshow("width resized", resized)
cv2.waitKey(0)

resized = imutiles.resize(image, height=200)
cv2.imshow("height resized", resized)
cv2.waitKey(0)
