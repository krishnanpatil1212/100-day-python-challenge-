
import pandas as pd

df = pd.DataFrame({
    "Department":["IT","HR","IT","Sales","HR","IT"],
    "Salary":[50000,40000,60000,70000,45000,50000]
})

df["Bonus"] = df["Salary"] * 0.10

df["Tax"]=df["Salary"]*0.05

df["Total"] = df["Salary"] + df["Bonus"]

df["Department"] = df["Department"].replace("Sales", "FF")

print(df)


df.to_excel("Department.xlsx", index=False)

print("Excel file saved successfully!")