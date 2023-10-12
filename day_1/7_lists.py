# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Accessing elements by index
print("Accessing Elements:")
print("First element:", numbers[0])  # Access the first element (index 0)
print("Last element:", numbers[-1])  # Access the last element (index -1)
print("Third element:", numbers[2])  # Access the third element (index 2)
print()

# Slicing a list
print("Slicing a List:")
print("First three elements:", numbers[0:3])  # Slices from index 0 to 2 (exclusive)
print("Last three elements:", numbers[-3:])  # Slices the last three elements
print("Every second element:", numbers[::2])  # Slices with a step of 2
print()

# Modifying elements
print("Modifying Elements:")
numbers[4] = 99  # Modify an element by index
print("Updated list:", numbers)
print()

# Adding elements
print("Adding Elements:")
numbers.append(11)  # Append an element to the end
print("Appended 11:", numbers)
numbers.insert(2, 22)  # Insert 22 at index 2
print("Inserted 22 at index 2:", numbers)
print()

# Removing elements
print("Removing Elements:")
numbers.pop()  # Remove and return the last element
print("Removed last element:", numbers)
numbers.remove(22)  # Remove the first occurrence of 22
print("Removed first occurrence of 22:", numbers)
del numbers[1:3]  # Delete elements by slicing
print("Deleted elements at index 1 and 2:", numbers)
print()

# Finding elements
print("Finding Elements:")
index_of_6 = numbers.index(6)  # Find the index of 6
print("Index of 6:", index_of_6)
count_of_5 = numbers.count(5)  # Count occurrences of 5
print("Count of 5:", count_of_5)
print()

# Sorting
print("Sorting:")
numbers.sort()  # Sort the list in ascending order
print("Sorted in ascending order:", numbers)
numbers.sort(reverse=True)  # Sort in descending order
print("Sorted in descending order:", numbers)
print()

# Reversing
print("Reversing:")
numbers.reverse()  # Reverse the list in place
print("Reversed list:", numbers)
print()

# Copying lists
print("Copying Lists:")
new_numbers = numbers.copy()  # Create a shallow copy of the list
print("New list:", new_numbers)
print()

# Clearing a list
print("Clearing a List:")
numbers.clear()  # Clear all elements from the list
print("Cleared list:", numbers)
print()

# Calculate mean and standard deviation of a list of numbers
data = [15, 22, 13, 32, 25, 19, 18, 27, 21, 24]

# Calculate mean using Python list
mean = sum(data) / len(data)

# Calculate standard deviation without list comprehension
mean_diff_squared = []
for x in data:
    mean_diff_squared.append((x - mean) ** 2)

variance = sum(mean_diff_squared) / len(data)
std_deviation = variance ** 0.5

print("Mean (Python List):", mean)
print("Standard Deviation (Python List):", std_deviation)

# Calculate mean using NumPy
import numpy as np

# NumPy array
data = np.array([15, 22, 13, 32, 25, 19, 18, 27, 21, 24])

# Calculate mean using NumPy
mean = np.mean(data)

# Calculate standard deviation using NumPy
std_deviation = np.std(data)

print("Mean (NumPy Array):", mean)
print("Standard Deviation (NumPy Array):", std_deviation)
