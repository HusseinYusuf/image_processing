import cv2
import numpy as np

# Read an image (replace 'path/to/your/image.jpg' with the actual path to your image)
image = cv2.imread('/Users/hussef/Downloads/photo1682998779.jpeg', cv2.IMREAD_GRAYSCALE)

# Create a kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)

# Opening Operation
opening_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Closing Operation
closing_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Display the original and processed images
cv2.imshow('Original Image', image)
cv2.imshow('Opening Image', opening_image)
cv2.imshow('Closing Image', closing_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
