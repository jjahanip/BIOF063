# Basics of Image Manipulation with OpenCV

# Step 1: Install OpenCV
# If you haven't already, you can install OpenCV using pip:
# pip install opencv-python

# Step 2: Import the OpenCV library
import cv2

# Step 3: Load an image
image_path = "example.jpg"  # Replace with the path to your image
img = cv2.imread(image_path)

# Step 4: Display basic image properties
print("Image Shape:", img.shape)
print("Image Data Type:", img.dtype)

# Step 5: Show the image
cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 6: Convert the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 7: Resize the image
new_size = (200, 200)
img_resized = cv2.resize(img, new_size)
cv2.imshow("Resized Image", img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 8: Crop a portion of the image
x, y, w, h = 50, 50, 100, 100  # (x, y) is the top-left corner, (w, h) is the width and height of the region
img_cropped = img[y:y+h, x:x+w]
cv2.imshow("Cropped Image", img_cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 9: Rotate the image
angle = 45  # Rotate by 45 degrees
rows, cols, _ = img.shape
rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
img_rotated = cv2.warpAffine(img, rotation_matrix, (cols, rows))
cv2.imshow("Rotated Image", img_rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 10: Save the modified image
cv2.imwrite("grayscale_image.jpg", img_gray)
cv2.imwrite("resized_image.jpg", img_resized)
cv2.imwrite("cropped_image.jpg", img_cropped)
cv2.imwrite("rotated_image.jpg", img_rotated)
