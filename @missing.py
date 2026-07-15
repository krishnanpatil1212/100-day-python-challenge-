
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name":["Krishna","Rahul",None,"Amit","Rahul"],
    "Age":[21,np.nan,23,24,22],
    "Salary":[30000,40000,50000,None,40000]
})

print(df)

print(df.isnull())

print(df.isnull().sum())

print(df.notnull())

print(df.dropna())

print(df.fillna(0))
 
df["Age"]=df["Age"].fillna(
    df["Age"].mean()
)
print(df)

print(df.duplicated())

print(df.drop_duplicates())

print(
    df.drop_duplicates(
        subset="Name"
    )
)