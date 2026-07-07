
import pandas as pd

df=pd.read_csv("employee.csv")

df=df.rename(columns={"Salary":"Income"})

df.insert(2,"Bonus",[5000,6000,7000,8000])

df=df.assign(Total=df["Income"]+df["Bonus"])

df["Age"]=df["Age"].astype(float)

print(df)