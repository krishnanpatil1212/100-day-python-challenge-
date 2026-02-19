from functools import reduce

nums=[1,2,3,4,5,6]

doubled=list(map(lambda x: x*2,nums))

even=list(filter(lambda x: x%2==0,doubled))

total=reduce(lambda a, b: a+b, even)

print("Doubled:", doubled)
print("Even:", even)
print("Total:", total)

