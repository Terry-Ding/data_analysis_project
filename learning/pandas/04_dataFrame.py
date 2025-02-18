import pandas as pd
import numpy as np

# Create a DataFrame using numpy array and reshape it to 3 rows and 4 columns
df = pd.DataFrame(np.arange(12).reshape(3, 4), index = list("abc"), columns = list("wxyz"))

print(df)
print()

d1 = {
    "name": ["xiaoming", "xiaohon"],
    "age": [20, 32],
    "tel": [10086, 10010]
}
df2 = pd.DataFrame(d1)
print(df2)