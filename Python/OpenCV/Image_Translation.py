import cv2
import numpy as np

img = cv2.imread("C://Users/Thomas/Documents/Downloads/nuig.jpg", 0)

rows, cols = img.shape

# Translation matrix (x and y never change)
m = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, m, (cols, rows))

cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
