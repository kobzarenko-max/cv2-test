import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

green = (0, 255, 0)
cv2.circle(canvas, (100, 100), 10, green)
cv2.imshow("Single circle", canvas)
cv2.waitKey(0)

red = (0, 0, 255, )
(centerX, centerY) = (canvas.shape[1]//2, canvas.shape[0]//2)

for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, red)

cv2.imshow(" h-h-he-hell-hello", canvas)
cv2.waitKey(0)


canvas = np.zeros((300, 300, 3), dtype="uint8")
for i in range(0, 25):
    radius = np.random.randint(5, high=250)
    color = np.random.randint(0, high=100, size=(3,)).tolist()
    pt = np.random.randint(0, high=200, size=(2,))
    cv2.circle(canvas, tuple(pt), radius, color, -1)
cv2.imshow("hello mike and ma =x", canvas)
cv2.waitKey(0)
