import argparse
import imutiles
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("--image", required=True, help="enter Path to the image")
args = vars(ap.parse_args())

image_name = args["image"]
image = cv2.imread(image_name)

rotated = imutiles.rotate(image, 180)
cv2.imshow("180 NOSE SCOPE", rotated)
cv2.waitKey(0)
