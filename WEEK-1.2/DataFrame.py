
# #example 1 - using default index
import pandas as pd
data={'apples':[3,2,0,1], 'orange':[9,3,7,2]}
df=pd.DataFrame(data)
print(df)


print("\n")

#example 2 - using index names
import pandas as pd
data={'apples':[3,2,0,1], 'orange':[9,3,7,2]}
df=pd.DataFrame(data, index=['ABC', 'DEF', 'GHI', 'JKL'])
print(df)


#example 3 - to find location 

import pandas as pd
data={'apples':[3,2,0,1], 'orange':[9,3,7,2]}
df=pd.DataFrame(data, index=['ABC', 'DEF', 'GHI', 'JKL'])
print()
print(df.loc['GHI'])      

# example 4 - dataframes using columns and rows

#cols
import pandas as pd
data={'col_1':[3,2,1,0], 'col_2':['a','b','c','d']}
df=pd.DataFrame.from_dict(data)
print(df)
print()

#rows
import pandas as pd
data={'row_1':[3,2,1,0], 'row_2':['a','b','c','d']}
df=pd.DataFrame.from_dict(data, orient='index')
print(df)
print()

#cols and rows
import pandas as pd
data={'row_1':[3,2,1,0], 'row_2':['a','b','c','d']}
df=pd.DataFrame.from_dict(data, orient='index', columns=['A','B','C','D'])
print(df)


#Adding columns and rows to a dataframe

#Columns addition
import pandas as pd
d={'one':pd.Series([1,2,3], index=['a','b','c']),
   'two':pd.Series([4,5,6,7], index=['a','b','c', 'd'])}
df=pd.DataFrame(d)

print("Adding a new column by passing a Series:")
df['three']=pd.Series([10,20,30], index=['a','b','c'])
print(df)

print("\nAdding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']
print(df)


#Columns deletion


