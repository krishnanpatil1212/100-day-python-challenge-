
import pandas as pd

df=pd.DataFrame({
    "Math":[80,90],
    "Science":[85,95]
},
index=["Krishna","Rahul"])

print("original")
print(df)

print("\nStack")
print(df.stack())

stacked=df.stack()

print(stacked)

print("\nunstack")

print(stacked.unstack())