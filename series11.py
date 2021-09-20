import pandas as pd
 #creating Series objects
c11= pd.Series(data=[30,40,50], index=['science','commerce','humanities'])
c12= pd.Series(data=[37,44,45], index=['science','commerce','humanities'])
# adding two objects to get total no.of students
print("total no.of students")
print(c11+c12)# Series objects arithematic
