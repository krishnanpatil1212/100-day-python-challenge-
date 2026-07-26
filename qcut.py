
import pandas as pd

salary=[20000,30000,40000,50000,60000,70000,80000,90000]

df=pd.DataFrame({
    "Salary":salary
})

df["Level"]=pd.qcut(
    df["Salary"],
    q=4,
    labels=["Low","Medium","High","Very High"]
)

print(df)
