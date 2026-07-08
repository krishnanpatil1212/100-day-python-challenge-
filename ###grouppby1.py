
import pandas as pd

df=pd.read_csv("employee2.csv")

print("Average Salary")
print(df.groupby("Department")["Salary"].mean())

print("\n Maximum Salary")
print(df.groupby("Department")["Salary"].max())

print("\nTotal Salary")
print(df.groupby("Department")["Salary"].sum())

print("\nEmployee count")
print(df.groupby("Department").size())

df["Dept_Avg"]=df.groupby("Department")["Salary"].transform("mean")

print("\nupdated data")
print(df)