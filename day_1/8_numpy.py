# Step 1: Installation
# You need to install NumPy first if it's not already installed.
# You can install it using pip:
# pip install numpy

# Step 2: Import NumPy
import numpy as np

# Step 3: Creating NumPy Arrays

# Create a 1D array (vector)
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr1)
print()

# Create a 2D array (matrix)
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:")
print(arr2)
print()

# Step 4: Basic Array Operations

# Accessing elements
print("Accessing Elements:")
print("Element at row 1, column 2:", arr2[1, 2])
print()

# Slicing
print("Slicing:")
print("First row:", arr2[0, :])
print("Second column:", arr2[:, 1])
print()

# Arithmetic operations
print("Arithmetic Operations:")
addition = arr1 + arr1
print("Addition:")
print(addition)
subtraction = arr1 - arr1
print("Subtraction:")
print(subtraction)
multiplication = arr1 * arr1
print("Multiplication:")
print(multiplication)
division = arr1 / arr1
print("Division:")
print(division)
print()

# Step 5: Array Functions

# Mean and standard deviation
print("Mean of arr1:", np.mean(arr1))
print("Standard Deviation of arr1:", np.std(arr1))
print()

# Reshaping
print("Reshaping arr1:")
reshaped = arr1.reshape(5, 1)
print(reshaped)
print()

# IMAGES ARE ARRAYS
array = [[157, 153, 174, 168, 150, 152, 129, 151, 172, 161, 165, 166],
         [155, 182, 163, 74, 75, 62, 33, 17, 110, 210, 180, 154],
         [180, 180, 50, 14, 34, 6, 10, 33, 48, 105, 159, 181],
         [206, 109, 6, 124, 131, 111, 120, 204, 165, 15, 56, 180],
         [194, 68, 137, 251, 237, 239, 239, 228, 227, 87, 71, 201],
         [172, 106, 207, 233, 233, 214, 220, 239, 228, 98, 74, 206],
         [188, 88, 179, 209, 185, 215, 211, 158, 139, 75, 20, 169],
         [189, 97, 166, 84, 10, 168, 134, 11, 31, 62, 22, 148],
         [199, 168, 191, 193, 158, 227, 178, 143, 182, 106, 36, 190],
         [206, 174, 156, 252, 236, 231, 149, 178, 228, 43, 96, 234],
         [190, 216, 116, 149, 236, 187, 86, 150, 79, 38, 218, 241],
         [190, 224, 147, 108, 227, 210, 127, 102, 36, 101, 255, 224],
         [190, 214, 173, 63, 103, 143, 96, 50, 2, 109, 249, 215],
         [187, 196, 236, 75, 1, 81, 47, 0, 6, 217, 255, 211],
         [183, 202, 237, 145, 0, 0, 12, 108, 200, 138, 243, 236],
         [196, 206, 123, 207, 177, 121, 123, 200, 175, 13, 96, 218]
         ]
from matplotlib import pyplot as plt
plt.imshow(array, cmap='gray')
plt.show()