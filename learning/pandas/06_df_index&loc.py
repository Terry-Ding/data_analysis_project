import pandas as pd
import numpy as np

# Load the dataset into a DataFrame
df = pd.read_csv("data_analysis_project/learning/numpy/youtube_video_data/USvideos.csv")

"""
方括号写数组 表示取行 对行进行操作
方括号写字符串 表示取列索引 对列进行操作
"""

# Print the first 20 rows of the DataFrame
print("First 20 rows of the DataFrame:")
print(df[:20]) # Print the first 20 rows of the DataFrame

print()

# Print the 'title' column of the DataFrame
print("Title column of the DataFrame:")
print(df["title"]) # Print the 'title' column of the DataFrame

# pandas loc
"""
df.loc 通过 标签 获取行数据
"""
print()
print("pandas loc")

# Create a DataFrame with custom index and column labels
t3 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("wxyz"))
print("Custom DataFrame with index 'abc' and columns 'wxyz':")
print(t3)

# Access a specific element by row and column labels
print("Element at row 'a' and column 'z':")
print(t3.loc["a", "z"]) # Access the element at row 'a' and column 'z'

# Access a specific row by label
print("All columns of row 'a':")
print(t3.loc["a"]) # Access all columns of row 'a'

# Access a specific column by label
print("All rows of column 'y':")
print(t3.loc[:, "y"]) # Access all rows of column 'y'

# Access multiple rows and columns by labels
print("Rows 'a' and 'b' and columns 'w' and 'z':")
print(t3.loc[["a", "b"], ["w", "z"]]) # Access rows 'a' and 'b' and columns 'w' and 'z'

# pandas iloc
"""
df.iloc 通过 位置 获取行数据
"""
print()
print("pandas iloc")

# Print the DataFrame again for reference
print("Custom DataFrame with index 'abc' and columns 'wxyz':")
print(t3)

# Access a specific row by integer location
print("Second row (index 1):")
print(t3.iloc[1]) # Access the second row (index 1)

# Access a specific column by integer location
print("Third column (index 2):")
print(t3.iloc[:, 2]) # Access the third column (index 2)

# Access multiple columns by integer locations
print("Third and second columns (indices 2 and 1):")
print(t3.iloc[:, [2, 1]]) # Access the third and second columns (indices 2 and 1)

# Access multiple rows and columns by integer locations
print("First and third rows (indices 0 and 2) and third and second columns (indices 2 and 1):")
print(t3.iloc[[0, 2], [2, 1]]) # Access the first and third rows (indices 0 and 2) 
                                # and the third and second columns (indices 2 and 1)

# Access a slice of rows and columns
print("From the second row to the end and the first two columns:")
print(t3.iloc[1: , :2]) # Access from the second row to the end and the first two columns