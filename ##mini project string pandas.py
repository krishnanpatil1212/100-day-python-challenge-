
import pandas as pd

df = pd.read_csv("employee1.csv")

df["Name"]=df["Name"].str.strip()
df["Name"]=df["Name"].str.title()
df["Name"]=df["Name"].str.upper()

print(df)

print("\nContains Rahul")
print(df[df["Name"].str.contains("Rahul")])