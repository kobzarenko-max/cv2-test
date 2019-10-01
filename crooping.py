import argparse
import imutiles
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("--image", required=True, help="enter Path to the image")
args = vars(ap.parse_args())

image_name = args["image"]
image = cv2.imread(image_name)
cv2.imshow("original image", image)

cropped = image[14:302, 130:200]
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)
