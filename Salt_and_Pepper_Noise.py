import cv2
import numpy as np

image = cv2.imread('/Users/hussef/Downloads/photo1682998779.jpeg')

# Adding salt and pepper noise
salt_pepper_image = image.copy()
rows, cols, _ = salt_pepper_image.shape
num_salt = int(0.02 * image.size)
coords = [np.random.randint(0, i, num_salt) for i in (rows, cols, 2)]  # Include channel dimension
salt_pepper_image[tuple(coords)] = 1

cv2.imshow('Original Image', image)
cv2.imshow('Salt and Pepper Image', salt_pepper_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
