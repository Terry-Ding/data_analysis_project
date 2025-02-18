import pandas as pd
import numpy as np

# Load the dataset into a DataFrame
df = pd.read_csv("data_analysis_project/learning/numpy/youtube_video_data/USvideos.csv")

# Create a DataFrame with a range of numbers, reshaped into 3 rows and 4 columns
t3 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("wxyz"))

# Add some null values
t3.loc['a', 'w'] = np.nan  # Set the value at row 'a' and column 'w' to NaN
t3.loc['b'] = np.nan       # Set all values in row 'b' to NaN

# Check for null values in the DataFrame
print("Null values in t3:")
print(pd.isnull(t3))  # Returns a DataFrame of the same shape with True for NaN values and False otherwise
print("\nNot null values in t3:")
print(pd.notnull(t3)) # Returns a DataFrame of the same shape with False for NaN values and True otherwise

# Drop rows with any NaN values
t3.dropna(axis=0, how="any", inplace=True)

# Check for null values in the modified DataFrame
print("\n" + "*" * 50 + " After dropping rows with NaN values " + "*" * 50)
print(pd.isnull(t3))  # Returns a DataFrame of the same shape with True for NaN values and False otherwise

print("\nFill NaN values using fillna method:")
t2 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("wxyz"))

# Add some null values
t2.loc['a', 'w'] = np.nan  # Set the value at row 'a' and column 'w' to NaN
t2.loc['b'] = np.nan       # Set all values in row 'b' to NaN

# Fill NaN values in column 'w' with the mean of that column
t2.fillna(t2.mean(), inplace=True)
print(t2)  # Print the DataFrame after filling NaN values

print("\nFill NaN values in specific column 'w':")
t1 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("wxyz"))

# Add some null values
t1.loc['a', 'w'] = np.nan  # Set the value at row 'a' and column 'w' to NaN
t1.loc['b'] = np.nan       # Set all values in row 'b' to NaN

# Fill NaN values in column 'w' with the mean of that column
t1["w"] = t1["w"].fillna(t1["w"].mean())
print(t1)  # Print the DataFrame after filling NaN values in column 'w'