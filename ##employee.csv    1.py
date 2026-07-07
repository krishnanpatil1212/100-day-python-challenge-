
import pandas as pd

df=pd.read_csv("employee.csv")
print(df)

print(df.sum(numeric_only=True))

print(df.mean(numeric_only=True))

print(df.median(numeric_only=True))

print(df.mode())

print(df.min())

print(df.std(numeric_only=True))

print(df.var(numeric_only=True))

print(df.count())

print(df.corr(numeric_only=True))