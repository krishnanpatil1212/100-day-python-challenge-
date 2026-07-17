
import pandas as pd 

df = pd.DataFrame({
    "Name":["Krishna","Rahul","Amit"],
    "Salary":[30000,40000,50000]
})

df["NewSalary"]=df["Salary"].apply(
    lambda x: x* 1.10
)
print(df)
