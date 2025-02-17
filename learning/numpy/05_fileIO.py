import numpy as np

us_filename = "data_analysis_project/learning/numpy/youtube_video_data/US_video_data_numbers.csv"
uk_filename = "data_analysis_project/learning/numpy/youtube_video_data/GB_video_data_numbers.csv"

t1 = np.loadtxt(us_filename, delimiter = ",", dtype = "int")
print(t1)
t2 = np.loadtxt(us_filename, delimiter = ",", dtype = "int", unpack = True) # unpack转置
print("*" * 100)
print(t2)