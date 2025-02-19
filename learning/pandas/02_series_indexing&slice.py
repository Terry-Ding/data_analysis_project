import pandas as pd

# Create a dictionary
temp_dict = {
    "name": "xiaoming",
    "age": 30,
    "tel": 10086
}

# Convert the dictionary to a Pandas Series
t1 = pd.Series(temp_dict)

# Print a separator
print("*" * 10)

# Print the entire Series
print(t1)
print()

# Access and print elements by index
print("Element at index 1:", t1[1])  # Access the element with index 1
print("Element at index 2:", t1[2])  # Access the element with index 2
print("*" * 10)

# Print the index of the Series (keys)
print(t1.index)

# Print the length of the index
print(len(t1.index))

# Print the values of the Series
print(t1.values)