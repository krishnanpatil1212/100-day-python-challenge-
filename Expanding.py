
import pandas as pd

df=pd.DataFrame({
    "Sales":[100,120,150,130,170]
})

df["Expanding Sum"]=df["Sales"].expanding().sum()

df["Expanding Average"]=df["Sales"].expanding().mean()

df["Expanding Max"]=df["Sales"].expanding().max()

df["Expanding Min"]=df["Sales"].expanding().min()

df["Expanding Median"]=df["Sales"].expanding().median()

df["Expanding STD"]=df["Sales"].expanding().std()

print(df)