import pandas as pd
import numpy as np

# Create a DataFrame using numpy array and reshape it to 3 rows and 4 columns
df = pd.DataFrame(np.arange(12).reshape(3, 4))
print(df)