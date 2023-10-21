import cv2

# Load the image
image = cv2.imread('/Users/hussef/Downloads/photo1645111760.jpeg')

# Define the rotation angle (in degrees)
angle = 45  # You can change this value as needed

# Get the center of the image (assumes the image is square)
height, width = image.shape[:2]
center = (width / 2, height / 2)

# Create a rotation matrix
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

# Apply the rotation matrix to the image
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Display or save the rotated image
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# If you want to save the rotated image to a file
cv2.imwrite('rotated_image.jpg', rotated_image)