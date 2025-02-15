import pandas as pd

t1 = pd.Series([1, 2, 3, 4, 5])
print(t1)

t2 = pd.Series([1, 23, 2, 2, 1], index = list("abcde"))
print(t2)