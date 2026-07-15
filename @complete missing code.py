
import pandas as pd
import numpy as np

df=pd.DataFrame({
    "Name":["Krishna","Rahul",None,"Amit","Rahul"],
    "Age":[21,np.nan,23,24,22],
    "Salary":[30000,40000,50000,None,40000]
})

print("original Data")
print(df)

print("\nmissing values")
print(df.isnull().sum())

df["Age"]=df["Age"].fillna(
    df["Age"].mean()
)

df["Salary"]=df["Salary"].fillna(
    df["Salary"].mean()
)

print("\nafter cleaning")
print(df)

print("\nduplicate")
print(df.duplicated())

df = df.drop_duplicates()

print("\nfinal Data")
print(df)