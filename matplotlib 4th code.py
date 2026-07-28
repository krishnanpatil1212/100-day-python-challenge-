
import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun"]
profit = [12000,18000,15000,22000,25000,28000]

plt.plot(
    months,
    profit,
    color="green",
    marker="o"
)

plt.title("COMPANY PROFIT REPORT")
plt.xlabel("months")
plt.ylabel("profit ($)")

plt.grid(True)

plt.show()