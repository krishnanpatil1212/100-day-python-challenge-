
import pandas as pd

df=pd.DataFrame({
    "Name":["Krishna","Rahul","Amit"],
    "Salary":[30000,40000,50000],
    "Department":["IT","HR","Sales"]
})

df["NewSalary"]=df["Salary"].apply(
    lambda x: x*1.20
)

df["Name"]=df["Name"].apply(str.upper)

dept={
    "IT":"Technology",
    "HR":"Human Resource",
    "Sales":"Marking"
}

df["Department"]=df["Department"].map(dept)

print(df)