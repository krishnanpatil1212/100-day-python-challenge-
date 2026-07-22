
import pandas as pd

employee={
    "Department":["IT","HR","Sales","HR","IT","IT"],
    "Salary":[50000,40000,60000,70000,45000,50000]
}
df=pd.DataFrame(employee)

print("original Data")
print(df)

print("\nDepartment count")
print(df["Department"].value_counts())

print("\nunique Department")
print(df["Department"].unique())

print("\nnumber of unique Departments")
print(df["Department"].nunique())

print("\nSalary count")
print(df["Salary"].value_counts())

print(df.groupby("Department")["Salary"].mean())

print(df.groupby("Department")["Salary"].sum())

print(df.groupby("Department")["Salary"].max())

print(df.groupby("Department")["Salary"].min())

print(df.groupby("Department")["Salary"].count())

print(df["Salary"].mean())

print(df["Salary"].max())

print(df["Salary"].min())

print(df["Salary"].median())

print(df["Department"].replace("Sales","FF"))

print(df)