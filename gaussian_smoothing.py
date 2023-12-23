import cv2

image = cv2.imread('/Users/hussef/Downloads/photo1682998779.jpeg')
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
