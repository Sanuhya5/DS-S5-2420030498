#ex-6 removing duplicates

import pandas as pd
df = pd.DataFrame({'ID' : [1,2,2,3,4,4],
                   'Name' : ['Alice','Bob','Bob','Charlie','David','David'],
                   'Age' : [25,30,30,35,40,40]
})
print()
print("Original Dataset:\n",df )
df_exact = df.drop_duplicates()
print("\nAfter removing duplicates:\n",df_exact)

#ex-7 subsets

import pandas as pd
df = pd.DataFrame({'ID' : [1,2,2,3,4,4],
                   'Name' : ['Alice','Bob','Bob','Charlie','David','David'],
                   'Age' : [25,30,30,35,40,40]
})
print("Original Data:\n", df)

#remove duplicates based on id
df_subset_id=df.drop_duplicates(subset=['ID'])
print("\n After subset based removal(ID): \n", df_subset_id)

#remove duplicates based on name
df_subset_name=df.drop_duplicates(subset=['Name'])
print("\n After subset based removal(Name):\n", df_subset_name)