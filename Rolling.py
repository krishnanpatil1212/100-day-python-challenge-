
import pandas as pd

df=pd.DataFrame({
    "Day":[1,2,3,4,5,6,7],
    "Sales":[100,120,150,130,170,180,200]
})

df["Rolling Average"]=df["Sales"].rolling(3).mean()

df["Rolling Sum"]=df["Sales"].rolling(3).sum()

df["Rolling Max"]=df["Sales"].rolling(3).max()

df["Rolling Min"]=df["Sales"].rolling(3).min()

df["Rolling Median"]=df["Sales"].rolling(3).median()

df["Rolling STD"]=df["Sales"].rolling(3).std()

print(df)

