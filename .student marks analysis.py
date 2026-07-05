import numpy as np

marks = np.array([
    [85,90,78],
    [70,88,92],
    [95,89,96],
    [60,75,80]
    ])

print("marks matrix:")
print(marks)

student_avg=np.mean(marks, axis=1)
print("\nstudent average:")
print(student_avg)

student_avg=np.mean(marks, axis=0)
print("\nsubject average:")
print(student_avg)

print("\nhighest mark:")
print(np.max(marks))

print("\nlowest marks:")
print(np.min(marks))

print("\nstudents with average >85:")
print(student_avg[student_avg>85])
