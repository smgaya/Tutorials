import cv2

img = cv2.imread("C://Users/Thomas/Documents/Downloads/nuig.jpg", 0)
rows, cols = img.shape

m = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
dst = cv2.warpAffine(img, m, (cols, rows))

cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
