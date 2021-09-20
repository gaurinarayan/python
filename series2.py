import pandas as pd
staff=pd.Series([20,36,44])
salaries=pd.Series([16000,24600,56300])
average=salaries/staff
d={"no of people":staff,"income":salaries,'avg':average}
df=pd.DataFrame(d)
print(df)
print(df["no of people"]<40)







print(df.describe())
