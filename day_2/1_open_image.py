from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Open the image
image_path = "imgs/abraham.png"
img = Image.open(image_path)

# Convert the image to numpy array
img = np.array(img)

# show image
plt.imshow(img, cmap="gray")
plt.show()