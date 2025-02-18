import pandas as pd
# Load the dataset into a DataFrame
df = pd.read_csv("data_analysis_project/learning/numpy/youtube_video_data/USvideos.csv")

# Split the tags column by '|' and print the result
tags_li = df["tags"].str.split("|").tolist()
print(tags_li)