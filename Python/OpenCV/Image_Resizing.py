import cv2

img = cv2.imread("C://Users/Thomas/Documents/Downloads/nuig.jpg")

res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

#OR

height, width = img.shape[:2]
res = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_CUBIC)