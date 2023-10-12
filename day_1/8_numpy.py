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

# Step 6: Conclusion
print("NumPy is a powerful library for numerical computations in Python.")
