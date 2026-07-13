
import pandas as pd

sales=pd.DataFrame({
    "Month":["Jan","Jan","Fed","Fed"],
    "product":["Laptop","Phone","Laptop","Phone"],
    "Sales":[100,200,150,250]
})

result = pd.pivot_table(
    sales,
    values="Sales",
    index="Month",
    columns="product",
    aggfunc="sum"
)

print(result)