import cv2

# Import Image
# img = cv2.imread("C://Users/Thomas/Documents/Downloads/nuig.jpg", cv2.IMREAD_COLOR)
# img = cv2.imread("C://Users/Thomas/Documents/Downloads/nuig.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("C://Users/Thomas/Documents/Downloads/nuig.jpg", cv2.IMREAD_UNCHANGED)
# Show Image
cv2.imshow('image', img)
k = cv2.waitKey(0)
# ESC
if k == 27:
    cv2.destroyAllWindows()
# Save
elif k == ord('s'):
    cv2.imwrite("C://Users/Thomas/Documents/Downloads/nuig_grey.jpg", img)
    cv2.destroyAllWindows()
