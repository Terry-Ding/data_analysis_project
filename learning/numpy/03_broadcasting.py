import numpy as np

t1 = np.array([[1, 2, 3, 4], [7, 8, 9, 10], [1, 2, 3, 4], 
               [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
t1 -= 1 # 每一个元素都会减1
print(t1)

t2 = np.arange(100, 124).reshape((4, 6))
print(t2)
print()
print(t1.reshape((4, 6)) + t2) # Broadcasting allows element-wise addition