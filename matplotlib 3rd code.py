
import matplotlib.pyplot as plt

students = ["A","B","C","D","E"]

marks = [78,92,85,70,88]

plt.plot(students,marks)

plt.xlabel("students")

plt.ylabel("marks")

plt.title("Students Marks")

plt.grid()

plt.show()