import cv2
import numpy as np

image = cv2.imread('/Users/hussef/Downloads/photo1682998779.jpeg', cv2.IMREAD_GRAYSCALE)

gamma_value = 1.5
gamma_corrected_image = np.power(image / 255.0, gamma_value) * 255.0

cv2.imshow('Original Image', image)
cv2.imshow('Gamma Corrected Image', gamma_corrected_image.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
