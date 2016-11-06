import cv2
import numpy

# Adding images
x = numpy.uint8([250])
y = numpy.uint8([10])
print cv2.add(x, y)     # 250 + 10 = 260 => 255
print x + y             # 250 + 10 = 260 % 256 = 4

# Image Blending
img1 = cv2.imread("C://Users/Thomas/Documents/Downloads/logos.jpg")
img2 = cv2.imread("C://Users/Thomas/Documents/Downloads/brick.jpg")
combo = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
cv2.imshow("Image Blending", combo)
cv2.waitKey(0)
cv2.destroyAllWindows()
