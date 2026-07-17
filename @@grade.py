
import pandas as pd

df =pd.DataFrame({
    "Marks":[95,70,45,88]

})

df["Grade"]=df["Marks"].apply(
    lambda x: "Pass" if x>=50 else "Fail"

)

print(df)