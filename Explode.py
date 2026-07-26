
import pandas as pd 

df=pd.DataFrame({
    "Name":["Krishna","Rahul"],
    "Skills":[
        ["Pythonn","SQL","Pandas"],
        ["Java","C++"]
    ]
})

print(df.explode("Skills"))