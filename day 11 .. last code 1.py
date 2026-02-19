from functools import reduce

nums = list(map(int, input("Enter numbers separated by space: ").split()))

doubled=list(map(lambda x: x*2,nums))

even=list(filter(lambda x: x%2==0,doubled))

total=reduce(lambda a, b: a+b, even)

print("Doubled:", doubled)
print("Even:", even)
print("Total:", total)

