
import matplotlib.pyplot as plt

marks=[85,75,90,60]

students=["Krishna","Rahul","Amit","Priya"]

plt.pie(
    marks,
    labels=students
)

plt.title("STUDENT MARKS")

plt.show()