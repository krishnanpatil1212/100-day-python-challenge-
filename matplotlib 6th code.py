
import matplotlib.pyplot as plt

products=["Laptop","Mobile","Tablet","Watch"]

sales=[120,250,90,180]

plt.barh(
    products,
    sales,
   
    
    alpha=0.6,
    label="sales",
    color=["red","blue","green","yellow"]
    )

plt.title("PRODUCT SALES")

plt.xlabel("product")

plt.ylabel("units sold")

plt.show()

