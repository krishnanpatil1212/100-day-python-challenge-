
import pandas as pd

employee={
    "Emp_ID":[101,102,103,104,105,106],
    "Name":["Krishna","Rahul","Amit","Priya","Rohan","Neha"],
    "Department":["IT","HR","IT","Sales","Finance","HR"],
    "Age":[22,24,25,28,30,26],
    "Salary":[50000,40000,65000,70000,55000,45000],
    "Experience":[1,2,3,5,4,2]
}

df=pd.DataFrame(employee)

print(df)

print(df.head())

print(df.tail())

print(df.info())

print(df.describe())

print(df["Salary"].sum())

print(df["Salary"].mean())

print(df["Salary"].max())

print(df["Salary"].min())

print(df["Salary"].std())

df["Bonus"]=df["Salary"]*0.10

df["Tax"]=df["Salary"]*0.05

df["Total Salary"]=df["Salary"]+df["Bonus"]-df["Tax"]

print(df)

print(df.sort_values("Salary"))

print(df.sort_values("Salary",ascending=False))

print(df.groupby("Department")["Salary"].mean())

print(df.groupby("Department")["Salary"].max())

print(df.groupby("Department")["Salary"].min())

print(
    df.groupby("Department")["Salary"].agg(
        ["mean","max","min","sum"]
    )
)

df["Department Average"]=df.groupby("Department")["Salary"].transform("mean")

print(df)

df["Rank"]=df["Salary"].rank(ascending=False)

print(df)

df["Previous Salary"]=df["Salary"].shift(1)

print(df)

df["Difference"]=df["Salary"].diff()

print(df)

df["Growth"]=df["Salary"].pct_change()*100

print(df)

df["Rolling Average"]=df["Salary"].rolling(3).mean()

print(df)

df["Running Total"]=df["Salary"].expanding().sum()

print(df)

dummy=pd.get_dummies(df["Department"],dtype=int)

print(dummy)

df["Department Code"]=pd.factorize(df["Department"])[0]

print(df)

df["Age Group"]=pd.cut(
    df["Age"],
    bins=[20,25,30,40],
    labels=["Young","Adult","Senior"]
)

print(df)

df["Salary Level"]=pd.qcut(
    df["Salary"],
    q=4,
    labels=["Low","Medium","High","Very High"]
)

print(df)

print(df["Department"].value_counts())

print(df["Department"].unique())

df.to_csv("Employee.csv",index=False)

df.to_excel("Employee.xlsx",index=False)

df.to_json("Employee.json")

df.to_pickle("Employee.pkl")

print(df)