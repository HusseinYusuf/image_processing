import cv2
import numpy as np

image = cv2.imread('/Users/hussef/Downloads/photo1682998779.jpeg')

# Define lower and upper bounds for the RGB segmentation
lower_bound = np.array([0, 0, 0], dtype="uint8")
upper_bound = np.array([100, 100, 100], dtype="uint8")

# Create a mask and apply it to the original image
mask = cv2.inRange(image, lower_bound, upper_bound)
segmented_image = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('Original Image', image)
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
