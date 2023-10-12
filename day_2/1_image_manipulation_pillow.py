# Basics of Image Manipulation with Pillow (PIL)

# Step 1: Install Pillow
# If you haven't already, you can install Pillow using pip:
# pip install Pillow

# Step 2: Import the Pillow library
from PIL import Image

# Step 3: Open an image
image_path = "example.jpg"  # Replace with the path to your image
img = Image.open(image_path)

# Step 4: Display basic image properties
print("Image Format:", img.format)
print("Image Mode:", img.mode)
print("Image Size:", img.size)

# Step 5: Show the image
img.show()

# Step 6: Convert the image to grayscale
img_gray = img.convert("L")
img_gray.show()

# Step 7: Resize the image
new_size = (200, 200)
img_resized = img.resize(new_size)
img_resized.show()

# Step 8: Crop a portion of the image
box = (50, 50, 150, 150)  # (left, upper, right, lower)
img_cropped = img.crop(box)
img_cropped.show()

# Step 9: Rotate the image
angle = 45  # Rotate by 45 degrees
img_rotated = img.rotate(angle)
img_rotated.show()

# Step 10: Save the modified image
img_gray.save("grayscale_image.jpg")
img_resized.save("resized_image.jpg")
img_cropped.save("cropped_image.jpg")
img_rotated.save("rotated_image.jpg")

# Step 11: Close the image
img.close()
