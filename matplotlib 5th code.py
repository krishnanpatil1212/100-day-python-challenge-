
import matplotlib.pyplot as plt

students = ["Krishna","Rahul","Amit","Priya","Rohan"]
marks = [95,82,75,90,88]

plt.plot(
    students,
    marks,
    color="blue",
    linestyle="--",
    linewidth=3,
    marker="*",
    markersize=12
)

plt.title("STUDENT MARKS ANALYSIS")

plt.xlabel("students")

plt.ylabel("marks")

plt.grid(True)

plt.show()