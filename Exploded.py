
import pandas as pd

df=pd.DataFrame({
    "Student":["A","B","C"],
    "Subjects":[
        ["Maths","Science"],
        ["English","Physics"],
        ["Computer"]
    ]
})

print(df)

print("\nExploded")

print(df.explode("Subjects"))