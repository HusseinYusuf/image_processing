import cv2

image = cv2.imread('/Users/hussef/Downloads/photo1682998779.jpeg', cv2.IMREAD_GRAYSCALE)
smoothed_image = cv2.medianBlur(image, 5)

cv2.imshow('Original Image', image)
cv2.imshow('Smoothed Image', smoothed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
