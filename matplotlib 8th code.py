
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

students=["Krishna","Rahul","Amit","Priya","Rohan","Sneha","Arjun","Neha","Krian","Anjali"]

marks=np.random.randint(40,101, size=10)

df=pd.DataFrame({
    "students":students,
    "marks":marks
})

print("student dataset")
print(df)

print("\nAverage marks:",df["marks"].mean())
print("Highest marks:",df["marks"].max())
print("Lowest marks:",df["marks"].min())

plt.figure(figsize=(10,5))
plt.bar(
    df["students"],
    df["marks"],
    color="skyblue",
    alpha=0.6,
    edgecolor="black"
)

plt.title("STUDENT MARKS ANALYSIS")

plt.xlabel("students")

plt.ylabel("marks")

plt.grid(axis="y")

plt.show()