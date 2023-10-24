import numpy as np
from skimage import io, color, exposure
from skimage.util import img_as_ubyte
import matplotlib.pyplot as plt

# Load an image from file
image = io.imread('imgs/IHC.png')
io.imshow(image)
io.show()

# Convert the image to grayscale
gray_image = color.rgb2gray(image)
gray_image = img_as_ubyte(gray_image)
io.imshow(gray_image, cmap='gray')
io.show()

# 0. plot the histogram of the image
def get_hist(image):
    hist = np.array([0] * 256)
    for row in image:
        for pixel in row:
            hist[pixel] += 1
    return hist

# plot the histogram of the image
hist = get_hist(gray_image)
plt.bar(range(256), hist)
plt.show()


def plot_image_and_hist(image, hist, title=None):
    fig, ax = plt.subplots(ncols=2, figsize=(16, 6))
    ax[0].imshow(image, cmap='gray')
    ax[0].axis('off')
    ax[1].bar(range(256), hist, width=5.0)
    ax[1].set_xlim([0, 256])
    plt.suptitle(title)
    plt.show()

# plot the image and its histogram side-by-side
plot_image_and_hist(gray_image, hist)

# 1. Histogram Equalization
equalized_image = exposure.rescale_intensity(gray_image)
equalized_image = img_as_ubyte(equalized_image)
equalized_image_hist = get_hist(equalized_image)
plot_image_and_hist(equalized_image, equalized_image_hist, title="Equalization")

# 2. Gamma Correction
gamma = 1.5  # Adjust the gamma value as needed
gamma_corrected_image = exposure.adjust_gamma(equalized_image, gamma)
gamma_corrected_image = img_as_ubyte(gamma_corrected_image)
gamma_corrected_image_hist = get_hist(gamma_corrected_image)
plot_image_and_hist(gamma_corrected_image, gamma_corrected_image_hist, title="Gamma Correction")

# 3. Logarithmic Correction
log = 1.5  # Adjust the log value as needed
logarithmic_corrected_image = exposure.adjust_log(equalized_image, log)
logarithmic_corrected_image = img_as_ubyte(logarithmic_corrected_image)
logarithmic_corrected_image_hist = get_hist(logarithmic_corrected_image)
plot_image_and_hist(logarithmic_corrected_image, logarithmic_corrected_image_hist, title="Logaritmic Correction")

# 4. Contrast Limited Adaptive Histogram Equalization (CLAHE)
clahe_corrected_image = exposure.equalize_adapthist(equalized_image, kernel_size=100, clip_limit=0.01)
clahe_corrected_image = img_as_ubyte(clahe_corrected_image)
clahe_corrected_image_hist = get_hist(clahe_corrected_image)
plot_image_and_hist(clahe_corrected_image, clahe_corrected_image_hist, title="Contrast Limited Adaptive Histogram Equalization (CLAHE)")
