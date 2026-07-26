
import pandas as  pd

age=[18,22,28,35,45,55,65]

df=pd.DataFrame({
    "Age":age
})

df["Group"]=pd.cut(
    df["Age"],
    bins=[0,20,40,60,100],
    labels=["Teen","Adult","Middle Age","Senior"]
)

print(df)