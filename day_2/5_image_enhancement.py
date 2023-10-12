import cv2
import numpy as np

# Load an image from file
image = cv2.imread('example.jpg')
cv2.imshow('Original Image', image)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 1. Histogram Equalization
equalized_image = cv2.equalizeHist(gray_image)
cv2.imshow('Histogram Equalization', equalized_image)

# 2. Gamma Correction
gamma = 1.5  # Adjust the gamma value as needed
gamma_corrected_image = cv2.pow((gray_image / 255.0), gamma)
gamma_corrected_image = (gamma_corrected_image * 255).astype('uint8')
cv2.imshow('Gamma Correction', gamma_corrected_image)

# 3. Shading Correction
smoothed_image = cv2.GaussianBlur(gray_image, (21, 21), 0)  # Adjust kernel size as needed
shading_corrected_image = cv2.divide(gray_image, smoothed_image, scale=256)
cv2.imshow('Shading Correction', shading_corrected_image)

# 4. Contrast Limited Adaptive Histogram Equalization (CLAHE)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))  # Adjust parameters as needed
clahe_image = clahe.apply(gray_image)
cv2.imshow('CLAHE', clahe_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
