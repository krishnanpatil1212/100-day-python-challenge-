marks=(45,67,89,34,56)

highest=marks[0]
lowest=marks[0]

for m in marks:
    if m>highest:
        highest=m
    if m<lowest:
        lowest=m

print("highest marks:",highest)
print("lower marks:",lowest)
