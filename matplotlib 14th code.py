
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

study_hours=np.random.randint(1,9,50)

marks=study_hours*10+np.random.randint(-5,6,50)

plt.figure(figsize=(8,5))

plt.scatter(
    study_hours,
    marks,
    c=marks,
    cmap="viridis",
    s=120
)

plt.colorbar(label="marks")

plt.title("STUDY HOURS vs MARKS")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.grid()

plt.show()