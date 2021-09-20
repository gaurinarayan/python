import pandas as pd
ds1=pd.Series([3,6,9,12,15])
ds2=pd.Series([2,4,6,8,10])
ds3 = pd.Series([0, 1, 1, 2, 3])
ds=ds1+ds2+ds3
print("add three series:")
print(ds)

print("subtract two series:")
ds=ds1-ds2
print(ds)

print("multiply two series:")
ds=ds1*ds2
print(ds)

print("divide series1 by series2")
ds=ds1/ds2
print(ds)