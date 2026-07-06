
import pandas as pd

employee={
    "Name":["A","B","C","D"],
    "Department":["IT","HR","IT","Sales"],
    "Salary":[50000,40000,60000,70000]
}

df=pd.DataFrame(employee)
print(df)

print("\nAverage salary")
print(df["Salary"].mean())

print("\nhighest Salary")
print(df["Salary"].max())

print("\nlowest Salary")
print(df["Salary"].min())

print("\nshape")
print(df.shape)

print("\ncolumns")
print(df.columns)

print("\nfirst 2 rows")
print(df.head(2))

print("\nlast 2 rows")
print(df.tail(2))

print("\nDepartment wise average salary")
print(df.groupby("Department")["Salary"].mean())

print("\nSalary greater than 50000")
print(df[df["Salary"]>=50000])