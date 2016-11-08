# Thomas Reaney
# Electronic & Computer Engineering Student
# National University of Ireland Galway

import cv2
import numpy as np

img = cv2.imread("C://Users/Thomas/Documents/Downloads/circle.jpg", 0)
# img = cv2.imread("C://Users/Thomas/Documents/Downloads/j.png", 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow("Erosian", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Gradient", gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()
