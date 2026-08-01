
import matplotlib.pyplot as plt

sales =[35,25,20,20]

products=["Laptop","Mobile","Tablet","Watch"]

explode=[0,0.2,0,0]

plt.pie(
    sales,
    labels=products,
    explode=explode,
    shadow=True,
    startangle=90,
    radius=1,
    wedgeprops={"edgecolor":"black","linewidth":2,"width":0.4,"edgecolor":"white"},
    colors=["red","blue","green","orange"],
    autopct="%1.1f%%"
)

plt.title("PRODUCT SALES")

plt.show()