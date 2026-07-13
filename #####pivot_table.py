
import pandas as pd

df = pd.DataFrame({
    "Department":["IT","IT","HR","HR"],
    "Salary":[30000,50000,40000,45000]
})

result=pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    aggfunc=["mean","max","min"]
)

print(result)