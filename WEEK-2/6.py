#ex 8 - case normalization(lowercase/uppercase)

import pandas as pd
df=pd.DataFrame({
    'Name':['Alice', 'BOB','charlie','DAVID']
})

#convert all to lcase
df['Name_lower']=df['Name'].str.lower()
print()

#convert all to ucase
df['Name_upper']=df['Name'].str.upper()
print(df)