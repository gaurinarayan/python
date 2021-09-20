import pandas as pd
section=['A','B','C','D']
contri=[6700,5600,5000,5200]
s=pd.Series(data=contri,index=section)
print(s)