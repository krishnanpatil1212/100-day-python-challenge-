
import pandas as pd

df = pd.DataFrame({
    "Name":["Krishna","Rahul","Amit","Rohan","Priya"],
    "Salary":[30000,40000,50000,60000,80000]
})

df["Rank"]=df["Salary"].rank()

df["Rank"]=df["Salary"].rank(ascending=False)

df["Salary"]=df["Salary"].clip(30000,70000)

print(df.where(df["Salary"]>45000))

print(df.mask(df["Salary"]>45000))

df["Previous_Salary"] = df["Salary"].shift(1)

df["Difference"]=df["Salary"].diff()

df["Growth"]=df["Salary"].pct_change()*100

print(df) 