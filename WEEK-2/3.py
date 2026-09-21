# ex 4 - drop rows with missing values

import pandas as pd
import numpy as np
#Sample dataset
df = pd.DataFrame({
    'Age':[25,40,50,np.nan,20],
    'Department': ['HR', 'Finance', 'Finance', np.nan,'IT']
    })

#Display original dataset
print("Original Dataset (With Missing Values):")
print()
print(df)

#Drop rows
print()
df_drop_rows=df.dropna()
print()
print("After dropping rows:\n", df_drop_rows)
print()

#ex 5 - for the whole column
df_drops_cols=df.dropna(axis=1)
print("After dropping rows:\n", df_drops_cols)


