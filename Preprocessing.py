
import pandas as pd

employee=pd.DataFrame({
    "Name":["Krishna","Rahul","Amit","Priya"],
    "Department":["IT","HR","Sales","IT"],
    "Age":[22,28,35,42],
    "Salary":[40000,55000,70000,85000]
})

print("original Data")
print(employee)

dummy=pd.get_dummies(employee["Department"],dtype=int)

print("\nOne Hot Encoding")
print(dummy)

employee["Department_Code"]=pd.factorize(employee["Department"])[0]

employee["Age Group"]=pd.cut(
    employee["Age"],
    bins=[0,25,35,50],
    labels=["Young","Adult","senior"]
)

employee["Salary Level"]=pd.qcut(
    employee["Salary"],
    q=4,
    labels=["Low","Medium","High","Very High"]
)

print("\nFinal Data")
print(employee  )