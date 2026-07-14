
import pandas as pd

df = pd.DataFrame({
    "Date":["2025-01-15","2025-05-20","2025-12-25"]
})

df["Date"]=pd.to_datetime(df["Date"])

df["Year"]=df["Date"].dt.year

df["Month"]=df["Date"].dt.month

df["Day"]=df["Date"].dt.day

df["Day_Name"]=df["Date"].dt.day_name()

df["Month_Name"]=df["Date"].dt.month_name()

print(df)