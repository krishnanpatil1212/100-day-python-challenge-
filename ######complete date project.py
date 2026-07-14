
import pandas as pd

df = pd.DataFrame({
    "Date":[
    "2025-01-15 10:30:45",
    "2025-05-20 15:20:10",
    "2025-12-25 08:45:30"
    ]
})

df["Date"]=pd.to_datetime(df["Date"])

df["Year"]=df["Date"].dt.year
df["Month"]=df["Date"].dt.month
df["Day"]=df["Date"].dt.day
df["Day_Name"]=df["Date"].dt.day_name
df["Month_Name"]=df["Date"].dt.month_name
df["Hour"]=df["Date"].dt.hour
df["Minute"]=df["Date"].dt.minute
df["Second"]=df["Date"].dt.second

print(df)
