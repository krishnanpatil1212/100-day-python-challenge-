
import matplotlib.pyplot as plt

hours=[2,3,4,5,6]

marks=[50,60,70,85,95]

colors=["red","blue","green","orange","purple"]

plt.scatter(
    hours,
    marks,
    c=colors,
    marker="*",
    s=200,
    alpha=0.5
)

plt.title("STUDY HOURS VS MARKS")

plt.xlabel("study hours")

plt.ylabel("marks")

plt.show()