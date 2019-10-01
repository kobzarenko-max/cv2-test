import argparse
import imutiles
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("--image", required=True, help="enter Path to the image")
args = vars(ap.parse_args())

image_name = args["image"]
image = cv2.imread(image_name)
cv2.imshow("original image", image)

flipped = cv2.flip(image, 0)
cv2.imshow("flipped one way", flipped)

flipped = cv2.flip(image, 1)
cv2.imshow("flipped other way", flipped)

flipped = cv2.flip(image, -1)
cv2.imshow("flipped both ways", flipped)

cv2.waitKey(0)