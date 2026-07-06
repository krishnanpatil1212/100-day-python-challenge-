
import pandas as pd

student ={
    "Name":["Krishna","Rahul","Manjunath","Harini"],
    "Age":[22,23,24,23],
    "Marks":[85,90,75,95]
}
df=pd.DataFrame(student)
print("student data")
print(df)

print("\nshape:")
print(df.shape)

print("\ncolumns:")
print(df.columns)

print("\nfirst 2 rows:")
print(df.head(2))

print("\nlast 2 rows:")
print(df.tail(2))

print("\nNames:")
print(df["Name"])

print("\nAge:")
print(df["Age"])

print("\nMarks>80:")
print(df[df["Marks"]>80])

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest marks:")
print(df["Marks"].max())

print("\nlowest marks:")
print(df["Marks"].min())