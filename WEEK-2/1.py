#Data quality issues

# ex-1 filling missing values using mean, mode, median

import pandas as pd
import numpy as np
#Sample dataset
df = pd.DataFrame({
    'Age':[25,40,50,np.nan,20],
    'Department': ['HR', 'Finance', 'Finance',np.nan, 'IT']
    })
print(df)
#Mean
df['Age']=df['Age'].fillna(df['Age'].mean())
#Mode for categorical
df['Department']=df['Department'].fillna(df['Department'].mode()[0])
print(df)


