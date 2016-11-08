# Thomas Reaney
# Electronic & Computer Engineering Student
# National University of Ireland Galway

import cv2

img1 = cv2.imread("C://Users/Thomas/Documents/Downloads/nuig.jpg", cv2.IMREAD_COLOR)
# Initial
e1 = cv2.getTickCount()

for i in xrange(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)

# Final
e2 = cv2.getTickCount()

# Execution time
print (e2 - e1)/cv2.getTickFrequency()

print cv2.useOptimized()

