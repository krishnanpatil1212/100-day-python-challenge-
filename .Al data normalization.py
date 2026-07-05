import numpy as np

data=np.array([
    [150,65],
    [160,70],
    [170,75],
    [180,80],
    [190,85]
    ])

print("original data:")
print(data)

min_values = np.min(data, axis=0)
max_values = np.max(data, axis=0)

normalized = (data - min_values)/(max_values - min_values)

print("\nNormalized data:")
print(normalized)
