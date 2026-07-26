
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
    "Salary":[50000,40000,60000,45000],
    "Bomus":[5000,4000,6000,4500]
},
index=index)

print("original Data")
print(df)

print("\nSwap Level")
print(df.swaplevel())

print("\nstack")
print(df.stack())

print("\nunstack")
print(df.stack().unstack())
