"""
from 11 years old to 30 years old
list a: the number of friends
y-axis: number
x-axis: age
"""

from matplotlib import pyplot as plt
fig = plt.figure(figsize=(12, 6), dpi = 100)

def analysis():
    a = [1, 0, 1, 1, 2, 4, 3, 2, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1]
    b = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    age_li = list(range(11, 31))

    plt.plot(age_li, a, label = "line 1", linestyle = '--', color = "orange")
    plt.plot(age_li, b, label = "line 2", color = "cyan", linewidth = 5)

    plt.xlabel("age")
    plt.ylabel("number")
    plt.xticks(range(11, 31), rotation = 45)
    plt.yticks(range(min(a), max(a) + 1), rotation = 45)

    # toggle grid
    plt.grid(alpha = 0.3) # alpha 透明度

    # 添加图例
    plt.legend()

    plt.savefig("data_analysis_project/learning/matplotlib/02_friend.png")
    plt.show()

analysis()