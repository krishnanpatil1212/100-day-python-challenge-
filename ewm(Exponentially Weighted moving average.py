
import pandas as pd

df=pd.DataFrame({
    "Sales":[100,120,150,130,170,180]
})

df["EWM"]=df["Sales"].ewm(span=3).mean()

print(df)