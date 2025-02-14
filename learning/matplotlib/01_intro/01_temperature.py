from matplotlib import pyplot as plt
import random

def plot1():
    fig = plt.figure(figsize=(18, 10), dpi=80)
    # x, y 一一对应
    x = range(2, 26, 2)
    y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]
    plt.plot(x, y)

    # x 轴刻度
    x_li = []
    for i in range(4, 49):
        x_li.append(i / 2)
    # plt.xticks(x_li) # more tight
    plt.xticks(x) # more reasonable
    plt.yticks(range(min(y), max(y) + 1))

    plt.show()

    # save file
    plt.savefig("learning/matplotlib/01temperature.png")

def plot2():
    fig = plt.figure(figsize=(18, 10), dpi=80)
    # 列表 a 表示 10点到 12点每一分钟到气温
    # 如何绘制折线图
    a = []
    for i in range(120):
        a.append(random.randint(20, 35))
    x = range(1, 121)

    plt.plot(x, a)
    
    # 添加 x 轴和 y 轴标签
    plt.xlabel('Time (minutes)')
    plt.ylabel('Temperature (°C)')
    
    plt.show()
    
    # 保存文件
    plt.savefig("learning/matplotlib/01temperature_2.png")

plot1()
plot2()