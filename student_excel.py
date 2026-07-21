
import pandas as pd

df = pd.DataFrame({
    "Name": ["Krishna", "Rahul"],
    "Age": [21, 22]
})

df.to_excel("output.xlsx", index=False)

print("Done")