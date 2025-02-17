import numpy as np

t1 = np.arange(12)
print(t1)
print(t1.shape)

t2 = np.array([[1, 2, 3], [4, 5, 6]])
print(t2)
print(t2.shape) # 两行三列

t3 = np.arange(12)
t3_reshaped = t3.reshape((3, 4)) # 变成三行四列的数组

t3_flatten = t3.flatten()

print(t3_reshaped)
print(t3_flatten)