import matplotlib.pyplot as plt
from skimage import io, filters, measure, color

# Load a biomedical image
image_path = 'imgs/img2.jpeg'  # Replace with your image path
image = io.imread(image_path)

# Display the original image
plt.figure(figsize=(6, 6))
plt.imshow(image, cmap='gray')
plt.axis('off')
plt.title('Original Image')
plt.show()

# 0. Convert to grayscale
image = color.rgb2gray(image)

# Display the grayscale image
plt.figure(figsize=(6, 6))
plt.imshow(image, cmap='gray')
plt.axis('off')
plt.title('Grayscale Image')
plt.show()

# 1. Thresholding (Otsu's method)
# https://en.wikipedia.org/wiki/Otsu%27s_method
threshold_value = filters.threshold_otsu(image)
binary_image = image > threshold_value

# Display the segmented binary image
plt.figure(figsize=(6, 6))
plt.imshow(binary_image, cmap='gray')
plt.axis('off')
plt.title('Thresholding (Otsu)')
plt.show()

# 2. Region-based Segmentation (Connected Components)
label_image = measure.label(binary_image)
image_label_overlay = color.label2rgb(label_image, image=image, bg_label=0)

# Display the labeled image
plt.figure(figsize=(6, 6))
plt.imshow(image_label_overlay)
plt.axis('off')
plt.title('Connected Components (Region-based Segmentation)')
plt.show()


