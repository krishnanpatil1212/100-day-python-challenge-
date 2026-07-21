
import pandas as pd

df = pd.DataFrame({
    "Name": ["John", "Alice", "Bob"],
    "Age": [25, 30, 35]
})

df.to_json("employees.json", orient="records", indent=4)

df = pd.read_json("employees.json")
print(df)

print("JSON file created!")