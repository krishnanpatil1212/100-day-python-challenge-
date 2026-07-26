
import pandas as pd 

index=pd.MultiIndex.from_tuples(
    [
        ("IT","Krishna"),
        ("IT","Rahul"),
        ("HR","Amit"),
        ("HR","Priya")
    ],
    names=["Department","Employee"]
)

df=pd.DataFrame({
    "Salary":[50000,40000,60000,45000]
}, index=index)

print(df)