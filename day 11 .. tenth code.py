from functools import reduce

nums=[1,3,4,5,6,7,8,9]
total=reduce(lambda a, b: a+b,nums)
print(total)
