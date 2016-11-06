import numpy
import cv2

# Black Image
img = numpy.zeros((512, 512, 3), numpy.uint8)
# Draw Circle
cv2.circle(img, (447, 63), 63, (0, 0, 255), 0)
# Show Image
cv2.imshow('image', img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
