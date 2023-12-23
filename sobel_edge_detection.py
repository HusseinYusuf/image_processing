import cv2
import numpy as np

image = cv2.imread('/Users/hussef/Downloads/photo1682998779.jpeg', cv2.IMREAD_GRAYSCALE)
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

cv2.imshow('Original Image', image)
cv2.imshow('Sobel Magnitude', sobel_magnitude.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
