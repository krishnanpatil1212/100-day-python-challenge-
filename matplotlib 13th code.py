
import matplotlib.pyplot as plt

experience=[1,2,3,4,5]

salary=[25000,35000,45000,65000,85000]

employees=[100,200,400,600,900]

plt.scatter(
    experience,
    salary,
    s=employees,
    c="green",
    alpha=0.6
)

plt.title("EXPERIENCE VS SALARY")

plt.xlabel("Experience")

plt.ylabel("Salary")

plt.show()