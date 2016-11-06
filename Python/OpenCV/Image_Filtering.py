import cv2
import numpy
from matplotlib import pyplot as plt

img = cv2.imread("C://Users/Thomas/Documents/Downloads/google.png")

kernel = numpy.ones((5, 5), numpy.float32) / 25
dst = cv2.filter2D(img, -1, kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
