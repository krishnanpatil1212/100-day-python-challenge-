
import pandas as pd

df=pd.read_csv("employee2.csv")

print(df.groupby("Department")["Salary"].mean())

print(
    df.groupby("Department")["Salary"].agg(
        ["mean","max","min"]
    )
)

df["Dept_Avg"]=df.groupby("Department")["Salary"].transform("mean")
print(df)

result=df.groupby("Department").filter(
    lambda x: x["Salary"].mean()>4500
)
print(result)

print(df.groupby("Department").size())

print(df.groupby("Department")["Salary"].sum())