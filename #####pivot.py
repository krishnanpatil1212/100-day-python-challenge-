
import pandas as pd

df = pd.DataFrame({
    "Name":["Krishna","Krishna","Rahul","Rahul"],
    "Subject":["Math","Science","Math","Science"],
    "Marks":[90,85,80,88]
})

result = df.pivot(
    index="Name",
    columns="Subject",
    values="Marks"
)

print(result)