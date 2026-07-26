
import pandas as pd

df=pd.DataFrame({
    "Department":["IT","HR","Sales","IT"]
})

dummy = pd.get_dummies(df, dtype=int)

print(dummy)