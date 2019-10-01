import argparse
import imutiles
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("--image", required=True, help="enter Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

shifted = imutiles.translate(image, 0, 100)
cv2.imshow("shifted down image", shifted)
cv2.waitKey(0)
