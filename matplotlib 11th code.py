
import matplotlib.pyplot as plt

departments=["IT","HR","Sales","Finance","Marketing"]

budget=[500000,200000,350000,250000,150000]

explode=[0.1,0,0,0,0]

plt.figure(figsize=(8,8))

plt.pie(
    budget,
    labels=departments,
    autopct="%1.1f%%",
    shadow=True,
    startangle=90\
)

plt.title("COMPANY BUDGET DISTRIBUTION")

plt.show()