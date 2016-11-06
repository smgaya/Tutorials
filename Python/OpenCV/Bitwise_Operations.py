import cv2

# Load Images
img1 = cv2.imread("C://Users/Thomas/Documents/Downloads/nuig.jpg")
img2 = cv2.imread("C://Users/Thomas/Documents/Downloads/google.png")

# Create ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# Create mask
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)

# Create inverse mask
mask_inv = cv2.bitwise_not(mask)

# Black out area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Use only parts of logo used in the logo image
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

# Add logo to ROI and modify main image
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

# Show image
cv2.imshow("Image with logo", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
