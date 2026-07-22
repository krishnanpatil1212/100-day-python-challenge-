
import pandas as pd

df=pd.DataFrame({
    "Department":["IT","HR","IT","Sales","HR","IT"],
    "Salary":[50000,40000,60000,70000,45000,50000]
})

print(df)

print(df["Department"].value_counts())

print(df["Department"].unique())

print(df["Department"].nunique())

print(df["Salary"].value_counts())

print(df["Salary"].mean())

print(df["Salary"].sum())      

print(df["Salary"].max())     

print(df["Salary"].min())     

print(df["Salary"].median()) 

print(df["Salary"].count()) 

print(df["Salary"].std())      

print(df.groupby("Department")["Salary"].mean())

print(df["Salary"].median()) 