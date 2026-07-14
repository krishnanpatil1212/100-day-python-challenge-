
import pandas as pd

df=pd.DataFrame({
    "Date":["2025-01-15 10:30:45",
            "2025-05-20 15:20:10"]
})

df["Date"]=pd.to_datetime(df["Date"])

df["Hour"]=df["Date"].dt.hour 

df["Minute"]=df["Date"].dt.minute

df["Second"]=df['Date'].dt.second

print(df)