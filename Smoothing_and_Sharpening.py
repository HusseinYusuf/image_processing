import cv2
import numpy as np

# Read an image (replace 'path/to/your/image.jpg' with the actual path to your image)
image = cv2.imread('/Users/hussef/Downloads/photo1682998779.jpeg', cv2.IMREAD_GRAYSCALE)

# Smoothing (Median Blur)
smoothed_image = cv2.medianBlur(image, 5)

# Sharpening
kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])
sharpened_image = cv2.filter2D(image, -1, kernel)

# Display the original and processed images
cv2.imshow('Original Image', image)
cv2.imshow('Smoothed Image', smoothed_image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
