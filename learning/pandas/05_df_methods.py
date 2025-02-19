import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_csv("data_analysis_project/learning/numpy/youtube_video_data/USvideos.csv")

# Print the entire DataFrame
print(df)
print("*" * 100)

# Print the first row of the DataFrame
print(df.head(1))
print("*" * 100)

# Print the last two rows of the DataFrame
print(df.tail(2))
print("*" * 100)

# Print a concise summary of the DataFrame
print(df.info())
print("*" * 100)

# Print descriptive statistics of the DataFrame
print(df.describe())