import numpy as np
import matplotlib.pyplot as plt
from skimage import io, filters, measure, color
from skimage.segmentation import active_contour, watershed
from skimage.feature import peak_local_max
from scipy import ndimage

# Load a biomedical image
image_path = 'biomedical_image.jpg'  # Replace with your image path
image = io.imread(image_path)

# Display the original image
plt.figure(figsize=(6, 6))
plt.imshow(image, cmap='gray')
plt.axis('off')
plt.title('Original Biomedical Image')
plt.show()

# 1. Thresholding (Otsu's method)
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

# 3. Active Contour (Snake) Segmentation
snake_points = np.array([[50, 50], [100, 100], [150, 50]])
snake = active_contour(image, snake_points, alpha=0.01, beta=0.1, gamma=0.001)

# Display the segmented boundary
plt.figure(figsize=(6, 6))
plt.imshow(image, cmap='gray')
plt.plot(snake[:, 0], snake[:, 1], '-r', lw=2)
plt.axis('off')
plt.title('Active Contour (Snake) Segmentation')
plt.show()

# 4. Watershed Segmentation
distance_map = ndimage.distance_transform_edt(binary_image)
local_maxima = peak_local_max(distance_map, indices=False, min_distance=20)
markers = ndimage.label(local_maxima)[0]
labels = watershed(-distance_map, markers, mask=binary_image)

# Display the segmented image
plt.figure(figsize=(6, 6))
plt.imshow(labels, cmap='nipy_spectral')
plt.axis('off')
plt.title('Watershed Segmentation')
plt.show()
