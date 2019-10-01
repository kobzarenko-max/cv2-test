import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("--image", required=True, help="enter Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])


(b, g, r) = image[0, 0]
print("Pixel at (0.0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
image[0, 0] = (0, 0, 255)


(b, g, r) = image[0, 0]
print("Pixel at (0.0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))


corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)
cv2.waitKey(0)


image[0:100, 0:100] = (0, 255, 0)
cv2.imshow("Updated", image)
cv2.waitKey(0)
