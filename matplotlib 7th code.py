
import matplotlib.pyplot as plt
import numpy as np

subjects=["Maths","Science","English"]

boys=[80,75,90]

girls=[85,82,88]

x=np.arange(len(subjects))

width=0.35

plt.bar(
    x-width/2,
    boys,
    width,
    label="Boys"
)

plt.bar(
    x+width/2,
    girls,
    width,
    label="Girls"
)

plt.xticks(x,subjects)

plt.title("Marks Comparison")

plt.xlabel("Subjects")

plt.ylabel("Marks")

plt.legend()

plt.grid(axis="y")

plt.show()