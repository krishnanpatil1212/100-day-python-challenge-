
import pandas as pd

employee=pd.DataFrame({
    "Name":["Krishna","Rahul","Amit"],
    "Salary":[50000,40000,60000],
    "Skills":[
        ["Python","SQL"],
        ["Java","C++"],
        ["AI","Machine Learning"]
    ]
})

print("original Data")
print(employee)

print("\nUsing T")
print(employee.T)

print("\nExploded Skills")
print(employee.explode("Skills"))