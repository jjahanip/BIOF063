# Basics of Image Manipulation with scikit-image (skimage)
# https://scikit-image.org/docs/stable/user_guide/getting_started.html

# Step 1: Install scikit-image
# If you haven't already, you can install scikit-image using pip:
# pip install scikit-image

# Step 2: Import the scikit-image library
import skimage.io as io
import skimage.color as color
from skimage.transform import resize, rotate
from skimage.util import img_as_ubyte

# Step 3: Load an image
image_path = "imgs/IHC.png"  # Replace with the path to your image
img = io.imread(image_path)

# Step 4: Display basic image properties
print("Image Shape:", img.shape)
print("Image Data Type:", img.dtype)

# Step 5: Display the image
io.imshow(img)
io.show()

# Step 6: Convert the image to grayscale
img_gray = color.rgb2gray(img)
img_gray = img_as_ubyte(img_gray)    # Convert to uint8 because skimgae uses float64 by default
io.imshow(img_gray, cmap='gray')
io.show()

# Step 7: Resize the image
new_size = (200, 200)
img_resized = resize(img, new_size, anti_aliasing=True)
img_resized = img_as_ubyte(img_resized)  # Convert to uint8 because skimgae uses float64 by default
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
img_rotated = img_as_ubyte(img_rotated)  # Convert to uint8 because skimgae uses float64 by default
io.imshow(img_rotated)
io.show()

# Step 10: Save the modified image

io.imsave("grayscale_image.png", img_gray)
io.imsave("resized_image.jpg", img_resized)
io.imsave("cropped_image.jpg", img_cropped)
io.imsave("rotated_image.jpg", img_rotated)
