from matplotlib import pyplot as plt

y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

x_3 = range(1, 32) # month
x_10 = range(51, 82)

plt.figure(figsize=(12, 8))
_x = list(x_3) + list(x_10)
x_ticks_labels = ["3.{} ".format(i) for i in x_3]
x_ticks_labels += ["10.{} ".format(j - 50) for j in x_10]
plt.xticks(_x[::3], x_ticks_labels[::3], rotation = 60) # 加步长，更开阔一些

plt.xlabel("time")
plt.ylabel("temperature")
plt.title("time & temp")

plt.scatter(x_3, y_3, label = "march")
plt.scatter(x_10, y_10, label = "october")
plt.legend()
plt.savefig("data_analysis_project/learning/matplotlib/03_scatter.png")
plt.show()