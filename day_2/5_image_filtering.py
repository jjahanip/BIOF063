import cv2

# Load an image from file
image = cv2.imread('imgs/IHC.png')

# Display the original image
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# 1. Gaussian Filter
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imshow('Gaussian Blur', blurred_image)
cv2.waitKey(0)

# 2. Median Filter
median_filtered_image = cv2.medianBlur(image, 15)
cv2.imshow('Median Filter', median_filtered_image)
cv2.waitKey(0)

# 3. Bilateral Filter
bilateral_filtered_image = cv2.bilateralFilter(image, 15, 75, 75)
cv2.imshow('Bilateral Filter', bilateral_filtered_image)
cv2.waitKey(0)

# 4. Thresholding
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresholded_image = cv2.threshold(gray_image, 50, 255, cv2.THRESH_BINARY)
cv2.imshow('Thresholding', thresholded_image)
cv2.waitKey(0)

# 5. Morphological Operations (Dilation)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
opened_image = cv2.morphologyEx(thresholded_image, cv2.MORPH_DILATE, kernel)
cv2.imshow('Morphological Dilation', opened_image)
cv2.waitKey(0)

# 6. Morphological Operations (Erosion)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
closed_image = cv2.morphologyEx(thresholded_image, cv2.MORPH_ERODE, kernel)
cv2.imshow('Morphological Erosion', closed_image)
cv2.waitKey(0)

# 7. Morphological Operations (Opening)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
opened_image = cv2.morphologyEx(thresholded_image, cv2.MORPH_OPEN, kernel)
cv2.imshow('Morphological Opening', opened_image)
cv2.waitKey(0)

# 8. Morphological Operations (Closing)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
closed_image = cv2.morphologyEx(thresholded_image, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Morphological Closing', closed_image)
cv2.waitKey(0)

# 9. Background Subtraction
image = cv2.imread('imgs/IHC.png', cv2.IMREAD_GRAYSCALE)
cv2.normalize(image, image, 0, 255, cv2.NORM_MINMAX)
cv2.imshow("original", image)
cv2.waitKey(0)

# Apply Gaussian blur to the image to reduce the influence of background noise
blurred = cv2.GaussianBlur(image, (5, 5), 5)
cv2.imshow("blurred", blurred)
cv2.waitKey(0)

# Calculate the absolute difference between the original and blurred image to highlight
# the differences between the background and the objects
diff = cv2.absdiff(image, blurred)
cv2.imshow("diff", diff)
cv2.waitKey(0)

# Apply a threshold to segment objects from the background
_, thresholded = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)
cv2.imshow("thresholded", thresholded)
cv2.waitKey(0)

# Apply a morphological opening filter to remove small objects
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
opening = cv2.morphologyEx(thresholded, cv2.MORPH_OPEN, kernel)
cv2.imshow("opening", opening)
cv2.waitKey(0)

# Apply a morphological closing filter to connect small gaps
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20, 20))
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
cv2.imshow("closing", closing)
cv2.waitKey(0)

# Invert the binary image to create a mask for objects
mask = cv2.bitwise_not(closing)
cv2.imshow("background mask", mask)
cv2.waitKey(0)

# Apply the mask to the original image to show the background
background = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("background", background)
cv2.waitKey(0)

foreground = image - background

# Display the result
cv2.imshow('Background Removed Image', foreground)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Close all windows
cv2.destroyAllWindows()
