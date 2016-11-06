# Import the necessary packages
from numpy import round
import cv2

# Load the image, clone it for output, and then convert it to greyscale
image = cv2.imread("C://Users/Thomas/Documents/Downloads/circle.jpg")
# image = cv2.imread("C://Users/Thomas/Documents/Downloads/circle2.jpg")
output = image.copy()
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect circle in the image
circles = cv2.HoughCircles(grey_image, cv2.cv.CV_HOUGH_GRADIENT, 1, 50, param1=125, param2=125, minRadius=0, maxRadius=0)

# Ensure at least some circles were found
if circles is not None:
    # Convert the (x, y) coordinates and radius of the circles to integers
    circles = round(circles[0, :]).astype("int")

    # Loop of the (x, y) coordinates and radius of the circles
    for (x, y, r) in circles:
        # Draw the circle in the output image
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        print r
        # Draw a rectangle in the center of the circle
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    # Show the output image
    cv2.imshow("output", output)
    cv2.waitKey(0)
