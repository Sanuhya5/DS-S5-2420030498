#ex-7 inconsistent formats

import pandas as pd
df=pd.DataFrame({
    'Date':['2025-01-05', '05/01/2025', 'Jan 5, 2025', '2025.09.08']
})
print("Original dataset:\n", df)
#convert all dates to standard iso format(yyyy-mm-dd)
df['Date']=pd.to_datetime(df['Date'], errors='coerce').dt.strftime('%Y-%m-%d')
print(df)