
import  pandas as pd

df=pd.DataFrame({
    "Name":["Krishna","Rahul"],
    "Math":[90,80],
    "Science":[85,88]
})

result=pd.melt(
    df,
    id_vars="Name",
    var_name="Subject",
    value_name="Marks"
)

print(result)