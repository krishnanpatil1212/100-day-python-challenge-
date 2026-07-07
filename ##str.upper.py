
import pandas as pd
df=pd.read_csv("employee1.csv")

df["City"]=df["City"].str.replace("banglore","mysore")

print(df)