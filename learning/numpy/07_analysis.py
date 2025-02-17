import numpy as np

# 加载国家数据
us_data = "data_analysis_project/learning/numpy/youtube_video_data/US_video_data_numbers.csv"
uk_data = "data_analysis_project/learning/numpy/youtube_video_data/GB_video_data_numbers.csv"

us_data = np.loadtxt(us_data, delimiter=",", dtype=int)
uk_data = np.loadtxt(uk_data, delimiter=",", dtype=int)

# 添加国家信息
# 构造全部为0的数据 (zero_data represents US data)
# us_data.shape[0] gives the number of rows in the us_data array
zero_data = np.zeros((us_data.shape[0], 1)).astype(int)
# 构造全部为1的数据 (ones_data represents UK data)
# uk_data.shape[0] gives the number of rows in the uk_data array
ones_data = np.ones((uk_data.shape[0], 1)).astype(int)

# 拼接两组
us_data = np.hstack((us_data, zero_data))
uk_data = np.hstack((uk_data, ones_data))

final_data = np.vstack((us_data, uk_data))
print(final_data)