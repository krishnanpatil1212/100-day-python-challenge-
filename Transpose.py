
import pandas as pd

df=pd.DataFrame({
    "Name":["Krishna","Rahul","Amit"],
    "Age":[21,22,23],
    "Salary":[50000,40000,60000]
})

print("original DataFrame")
print(df)

print("\nUsing T")
print(df.T)