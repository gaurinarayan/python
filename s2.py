import pandas as pd

arr = [31,28, 31, 30]

month = ["Jan", "Feb", "Mar", "Apr"]


s = pd.Series(data = arr, index = month)

print(s)

s = pd.Series(data = [32, 34, 35], index = ['A', 'B', 'C'])

print(s)



s = pd.Series(arr, index = month)



print(s)


s1 = pd.Series(range(1, 15,3), index = [x for x in 'abcde'])
print(s1)
