
import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May"]

sales = [1000,1500,2000,1800,2500]

plt.plot(months,sales)

plt.xlabel("months")

plt.ylabel("sales")

plt.title("Monthly Sales Report")

plt.grid()

plt.savefig("sales_report.png")

plt.show()