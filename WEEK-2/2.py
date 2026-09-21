#ex-2 Forward fill(use previous value)

import pandas as pd
import numpy as np
#Sample dataset
df = pd.DataFrame({
    'Age':[25,40,50,np.nan,20],
    'Department': ['HR', 'Finance', 'Finance', np.nan,'IT']
    })
#Display original dataset
print("Original Dataset (With Missing Values):")
print(df)
d_ffill=df.copy()
d_ffill.ffill(inplace=True)
print('\n Forward fill:')
print(d_ffill)

print()

#ex 3 - backward fill(use next value)

import pandas as pd
import numpy as np
#Sample dataset
df = pd.DataFrame({
    'Age':[25,40,50,np.nan,20],
    'Department': ['HR', 'Finance', 'Finance', np.nan,'IT']
    })
#Display original dataset
print("Original Dataset (With Missing Values):")
print(df)
d_bfill=df.copy()
d_bfill.bfill(inplace=True)
print('\n Backward fill:')
print(d_bfill)
