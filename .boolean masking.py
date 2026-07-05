import numpy as np


arr = np.array([10,20,30,40,50])

mask = arr>30

print(mask)
print(arr[mask])
