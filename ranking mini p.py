
import pandas as pd

df=pd.DataFrame({
    "Name":["Krishna","Rahul","Amit","Rohan","Priya"],
    "Salary":[50000,40000,60000,70000,45000]
})

df["Rank"]=df["Salary"].rank(ascending=False)

df["Bonus"]=df["Salary"]*0.10

df["Total"]=df["Salary"]+df["Bonus"]

df["Previous Salary"]=df["Salary"].shift(1)

df["Difference"]=df["Salary"].diff()

print(df)
