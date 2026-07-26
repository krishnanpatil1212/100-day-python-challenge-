
import pandas as pd

df=pd.DataFrame({
    "Department":["IT","HR","Sales","IT","HR"]
})

df["Code"]=pd.factorize(df["Department"])[0]

print(df)