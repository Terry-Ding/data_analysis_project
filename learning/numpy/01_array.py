import numpy as np
import random

t1 = np.array([1, 2, 3])
print(t1)
print(type(t1))

t2 = np.array(range(10))
print(t2)

t3 = np.arange(10) # equals to range
print(t3)
print(t3.dtype)

t4 = np.arange(4, 10, 2)
print(t4)

t5 = np.array([random.random() for i in range(10)])
print(t5)

t6 = np.round(t5, 2)
print(t6)