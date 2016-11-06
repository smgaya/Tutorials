import cv2

# Import Image
img = cv2.imread("C://Users/Thomas/Documents/Downloads/nuig.jpg", cv2.IMREAD_UNCHANGED)

# Access pixel value
print img[100, 100]

# Access only blue part of the pixel
print img[100, 100, 2]

# Modify pixel value
img[100, 100] = [255, 255, 255]
print img[100, 100]

# Access only red part of the pixel (faster)
print img.item(10, 10, 2)

# Modify red part of the pixel (faster)
img.itemset((10, 10, 2), 100)
print img.item(10, 10, 2)

# Number of rows, columns, channels (if image is colour)
print img.shape

# Number of pixels
print img.size

# Image datatype
print img.dtype

# Split blue, green, red values
b, g, r = cv2.split(img)

# Merge blue, green, red values
img = cv2.merge((b, g, r))
