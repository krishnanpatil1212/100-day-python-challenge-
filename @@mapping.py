
import pandas as pd

df=pd.DataFrame({
    "Department":["IT","HR","Sales"]
})

mapping={
    "IT":"Technology",
    "HR":"Human Resource",
    "Sales":"Marketing"
}

df["Department"]=df["Department"].map(mapping)

print(df)