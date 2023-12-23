import cv2

image = cv2.imread('/Users/hussef/Downloads/photo1682998779.jpeg', cv2.IMREAD_GRAYSCALE)
laplace_filtered_image = cv2.Laplacian(image, cv2.CV_64F)

cv2.imshow('Original Image', image)
cv2.imshow('Laplace Filtered Image', laplace_filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
