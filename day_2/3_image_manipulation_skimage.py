# Basics of Image Manipulation with scikit-image (skimage)

# Step 1: Install scikit-image
# If you haven't already, you can install scikit-image using pip:
# pip install scikit-image

# Step 2: Import the scikit-image library
import skimage.io as io
import skimage.color as color
from skimage.transform import resize, rotate

# Step 3: Load an image
image_path = "example.jpg"  # Replace with the path to your image
img = io.imread(image_path)

# Step 4: Display basic image properties
print("Image Shape:", img.shape)
print("Image Data Type:", img.dtype)

# Step 5: Display the image
io.imshow(img)
io.show()

# Step 6: Convert the image to grayscale
img_gray = color.rgb2gray(img)
io.imshow(img_gray, cmap='gray')
io.show()

# Step 7: Resize the image
new_size = (200, 200)
img_resized = resize(img, new_size, anti_aliasing=True)
io.imshow(img_resized)
io.show()

# Step 8: Crop a portion of the image
x, y, w, h = 50, 50, 100, 100  # (x, y) is the top-left corner, (w, h) is the width and height of the region
img_cropped = img[y:y+h, x:x+w]
io.imshow(img_cropped)
io.show()

# Step 9: Rotate the image
angle = 45  # Rotate by 45 degrees
img_rotated = rotate(img, angle, resize=True)
io.imshow(img_rotated)
io.show()

# Step 10: Save the modified image (if needed)
# Note: skimage does not provide a built-in save function, so you may need to use other libraries for saving images.

# If you need to save the modified images, you can use the io.imsave function from skimage.
# io.imsave("grayscale_image.jpg", img_gray)
# io.imsave("resized_image.jpg", img_res
