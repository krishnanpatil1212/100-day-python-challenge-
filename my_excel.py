
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "Name": ["Krishna", "Rahul", "Amit"],
    "Age": [21, 22, 23]
})

# Show data on screen
print(df)

# Save to Excel
df.to_excel("mydata.xlsx", index=False)

print("Excel file saved successfully!")