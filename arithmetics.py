import argparse
import numpy as np
import imutiles
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("--image", required=True, help="enter Path to the image")
args = vars(ap.parse_args())

image_name = args["image"]
image = cv2.imread(image_name)
cv2.imshow("original image", image)

print("max of 255 by cv2: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 0 by cv2: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))

print("wrap of max by np {}".format(np.uint8([200])+np.uint8([100])))
print("wrap of min by np: {}".format(np.uint8([50])-np.uint8([100])))

m = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, m)
cv2.imshow("added image", added)


m = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, m)
cv2.imshow("subtracted  image", subtracted)

cv2.waitKey(0)