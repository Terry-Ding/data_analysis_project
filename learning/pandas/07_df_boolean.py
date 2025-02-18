import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_csv("data_analysis_project/learning/numpy/youtube_video_data/USvideos.csv")

# Filter the DataFrame to include only rows where the comment_total is between 50000 and 60000
print(df[(df["comment_total"] > 50000) & (df["comment_total"] < 60000)])