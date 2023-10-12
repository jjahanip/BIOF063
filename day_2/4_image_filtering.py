import cv2

# Load an image from file
image = cv2.imread('example.jpg')

# Display the original image
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# 1. Gaussian Filter
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('Gaussian Blur', blurred_image)
cv2.waitKey(0)

# 2. Median Filter
median_filtered_image = cv2.medianBlur(image, 5)
cv2.imshow('Median Filter', median_filtered_image)
cv2.waitKey(0)

# 3. Bilateral Filter
bilateral_filtered_image = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Filter', bilateral_filtered_image)
cv2.waitKey(0)

# 4. Thresholding
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresholded_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Thresholding', thresholded_image)
cv2.waitKey(0)

# 5. Morphological Operations (Opening)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
opened_image = cv2.morphologyEx(thresholded_image, cv2.MORPH_OPEN, kernel)
cv2.imshow('Morphological Opening', opened_image)
cv2.waitKey(0)

# 6. Morphological Operations (Closing)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
closed_image = cv2.morphologyEx(thresholded_image, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Morphological Closing', closed_image)
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
