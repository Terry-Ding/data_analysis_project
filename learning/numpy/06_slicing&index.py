import numpy as np

us_filename = "data_analysis_project/learning/numpy/youtube_video_data/US_video_data_numbers.csv"
uk_filename = "data_analysis_project/learning/numpy/youtube_video_data/GB_video_data_numbers.csv"

t2 = np.loadtxt(us_filename, delimiter = ",", dtype = "int", unpack = True) # unpack转置
print(t2)
print("*" * 10)

print(t2[2]) # row
print(t2[2:]) # 连续的多行
print("*" * 10)

print(t2[:,0]) # column
print(t2[:,2:]) # 取连续的多列
print()
b = t2[2:5,1:4] # 第3行到第五行，第二列到第四列
print(b)