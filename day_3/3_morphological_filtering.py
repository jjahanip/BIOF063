import numpy as np
import matplotlib.pyplot as plt
from skimage import io, filters, morphology, measure, color

# Load a binary image
image_path = 'binary_image.jpg'  # Replace with your binary image path
binary_image = io.imread(image_path)

# Display the original image
plt.figure(figsize=(6, 6))
plt.imshow(binary_image, cmap='gray')
plt.axis('off')
plt.title('Original Binary Image')
plt.show()

# 1. Erosion and Dilation
eroded_image = morphology.binary_erosion(binary_image)
dilated_image = morphology.binary_dilation(binary_image)

plt.figure(figsize=(10, 4))
plt.subplot(131)
plt.imshow(binary_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(132)
plt.imshow(eroded_image, cmap='gray')
plt.title('Erosion')
plt.axis('off')
plt.subplot(133)
plt.imshow(dilated_image, cmap='gray')
plt.title('Dilation')
plt.axis('off')
plt.show()

# 2. Opening and Closing
np.random.seed(0)
noisy_image = np.zeros((100, 100), dtype=np.uint8)
noisy_image[30:70, 30:70] = 1
noisy_image += np.random.randint(0, 2, size=(100, 100))

opened_image = morphology.binary_opening(noisy_image)
closed_image = morphology.binary_closing(noisy_image)

plt.figure(figsize=(10, 4))
plt.subplot(131)
plt.imshow(noisy_image, cmap='gray')
plt.title('Noisy Image')
plt.axis('off')
plt.subplot(132)
plt.imshow(opened_image, cmap='gray')
plt.title('Opening')
plt.axis('off')
plt.subplot(133)
plt.imshow(closed_image, cmap='gray')
plt.title('Closing')
plt.axis('off')
plt.show()

# 3. Skeletonization
binary_shape = np.zeros((100, 100), dtype=np.uint8)
binary_shape[30:70, 40:60] = 1
skeleton = morphology.skeletonize(binary_shape)

plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.imshow(binary_shape, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(122)
plt.imshow(skeleton, cmap='gray')
plt.title('Skeletonization')
plt.axis('off')
plt.show()

# 4. Generating Quantitative Output
label_image = measure.label(binary_image)
num_objects = np.max(label_image)
image_label_overlay = color.label2rgb(label_image, image=binary_image, bg_label=0)

plt.figure(figsize=(8, 4))
plt.subplot(121)
plt.imshow(binary_image, cmap='gray')
plt.title('Binary Image')
plt.axis('off')
plt.subplot(122)
plt.imshow(image_label_overlay)
plt.title(f'Number of Objects: {num_objects}')
plt.axis('off')
plt.show()
