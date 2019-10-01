import numpy as np
import cv2


canvas = np.zeros((300, 300, 3), dtype="uint8")

green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("The line 1", canvas)
cv2.waitKey(0)


red = (0, 0, 255)
cv2.line(canvas, (0, 0), (300, 300), red, 3)
cv2.imshow("The line 2", canvas)
cv2.waitKey(0)


blue = (255, 0, 0)
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("The rec 1", canvas)
cv2.waitKey(0)


red = (0, 0, 255)
cv2.rectangle(canvas, (10, 10), (60, 60), red, 3)
cv2.imshow("The rec 2", canvas)
cv2.waitKey(0)


blue = (255, 0, 0)
cv2.rectangle(canvas,  (10, 10), (60, 60), blue, -1)
cv2.imshow("The rec 3", canvas)
cv2.waitKey(0)
