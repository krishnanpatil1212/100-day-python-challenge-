
import pandas as pd
df=pd.read_csv("employee1.csv")

df["City"]=df["City"].str.replace("bangalore","mysore")

print(df[df["Name"].str.contains("Rahul",case=False)])

print(df["Name"].str.startswith("R"))

print(df["Name"].str.endswith("r"))

print(df["Name"].str.split())

df["Name"]=df["Name"].str.strip()

print(df)
