import cv2
import numpy as np

image = cv2.imread('/Users/hussef/Downloads/photo1682998779.jpeg', cv2.IMREAD_GRAYSCALE)

Q = 1.5
contraharmonic_mean_image = cv2.filter2D(image, -1, np.ones((5, 5))/(5*5), borderType=cv2.BORDER_CONSTANT)

cv2.imshow('Original Image', image)
cv2.imshow('Contraharmonic Mean Image', contraharmonic_mean_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
