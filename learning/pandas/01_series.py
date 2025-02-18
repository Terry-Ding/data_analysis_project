import pandas as pd

# Create a pandas Series from a list
t1 = pd.Series([1, 2, 3, 4, 5])
print(t1)
print(type(t1))

# Create a pandas Series with a custom index
t2 = pd.Series([1, 23, 2, 2, 1], index=list("abcde"))
print(t2)

# Create a pandas Series from a dictionary
temp_dict = {
    "name": "xiaoming",
    "age": 30,
    "tel": 10086
}
t3 = pd.Series(temp_dict)
print("*" * 10)
print(t3)