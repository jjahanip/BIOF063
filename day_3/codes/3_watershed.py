# source: https://docs.opencv.org/4.x/d3/db4/tutorial_py_watershed.html
# https://en.wikipedia.org/wiki/Watershed_(image_processing)#Watershed_by_flooding
# visualization: https://svi.nl/watershed

import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import color
from skimage. exposure import rescale_intensity, adjust_gamma

img = cv2.imread("imgs/img2.jpeg")

# convert image to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# normalize image
img = rescale_intensity(img)

# # correct contrast using gamma correction
img = adjust_gamma(img, gamma=0.75)

# plot the grayscale image
plt.figure()
plt.imshow(img, cmap='gray')
plt.show()

# Threshold image to binary using OTSU
ret1, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.figure()
plt.imshow(thresh, cmap='gray')
plt.show()

# Morphological operations to remove small noise
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

plt.figure()
plt.imshow(opening, cmap='gray')
plt.show()

# OPTIONAL: Remove cells touching image border
from skimage.segmentation import clear_border
opening = clear_border(opening)  # Remove edge touching grains

# Find the sure background region
sure_bg = cv2.dilate(opening, kernel, iterations=10)

plt.figure()
plt.imshow(sure_bg, cmap='gray')
plt.show()


# Finding sure foreground area using distance transform
# intensity of each pixel inside the foreground regions are changed to
# distance their respective distances from the closest 0 value (boundary).
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)

plt.figure()
plt.imshow(dist_transform, cmap='gray')
plt.show()

# Let us threshold the dist transform by portion of its max value.
# We select %10 of max value, but it might be different for each image.
# Small values will not separate cells (under-segmentation)
# High values willnot recognize some cells
ret2, sure_fg = cv2.threshold(dist_transform, 0.1 * dist_transform.max(), 255, 0)

plt.figure()
plt.imshow(sure_fg, cmap='gray')
plt.show()

# Unknown region is background - foreground
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

plt.figure()
plt.imshow(sure_fg, cmap='gray')
plt.show()

plt.figure()
plt.imshow(unknown, cmap='gray')
plt.show()

# Now we create a marker and label the regions inside.
# For sure regions, both foreground and background will be labeled with positive numbers.
# Unknown regions will be labeled 0.
# Mark each object (connected component) with a number
ret3, markers = cv2.connectedComponents(sure_fg)

plt.figure()
plt.imshow(markers, cmap='jet')
plt.show()

# Watershed considers the unknown region with value 0; so, mark it with any value except 0.
# Add one to all labels so that sure background is not 0, but 1
markers = markers + 1

# Now, mark the region of unknown with zero
markers[unknown == 255] = 0

plt.figure()
plt.imshow(markers, cmap='jet')   #Look at the 3 distinct regions.
plt.show()

# convert the grayscale image to RGB format
img = np.dstack((img, img, img))

# Apply watershed algorithm
markers = cv2.watershed(img, markers)

# POST PROCESSING
#Set the edge pixels of image to 0
markers[0, :] = 1
markers[:, 0] = 1
markers[-1, :] = 1
markers[:, -1] = 1

# The boundary region will be marked -1
# We will change the color to red
boundary_image = np.copy(img)
boundary_image[markers == -1] = [255, 0, 0]

plt.figure()
plt.imshow(boundary_image)
plt.show()

label_image = color.label2rgb(markers, bg_label=1)

plt.figure()
plt.imshow(label_image)
plt.show()

# change the background label back to 0
markers[markers == -1] = 0
markers[markers == 1] = 0

# save the mask
# we usually save the masks as numpy array
np.save('mask.npy', markers)


# QUESTION: the borders are not smooth; How can we fix this?
