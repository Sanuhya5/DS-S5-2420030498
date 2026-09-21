# reading data from a csv file


#iris.csv file
import pandas as pd
df=pd.read_csv('Iris.csv') #method 1
print(df)
print()


#movies.csv file
import pandas as pd
df=pd.read_csv('movies.csv', index_col=0)  #another method for csv reading
print(df)


#titanic.csv file
import pandas as pd
df=pd.read_csv('titanic.csv', index_col=0)  #another method for csv reading
print(df)


#using json file
import pandas as pd
df=pd.read_json('sample1.json', typ='series')
print(df)
print()

#converting dataset to csv file/json file

import pandas as pd
data={'Student_no':[2420030498, 2420030427, 2420030505, 2420030592, 2420090101], 
'Student_name':['Sanuhya', 'Nimisha', 'Nikitha', 'Kumuda', 'Dhanu'],
'Student_age':[20, 19, 20, 20, 19],
'Section':['A', 'B', 'C', 'D', 'E'],
'Branch':['CSE', 'ECE', 'CIVIL', 'EEE', 'IT']}
df=pd.DataFrame(data)
print(df)

df.to_csv('student_details.csv') #converting to csv file

df.to_json('student_details.json') #converting to json file


#doing operations on csv file

import pandas as pd
df = pd.read_csv('Iris.csv')
print(df.head())
print()
print(df.head(10))
print()
print(df.tail())
print()
print(df.tail(10))
print()
df.info()
print()
print("Shape:")
print(df.shape)
print()
print("Description:")
print(df.describe())









