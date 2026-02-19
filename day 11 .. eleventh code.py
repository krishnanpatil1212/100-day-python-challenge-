from functools import reduce

nums=[1,2,3,4,5,6,7,8,9]
product=reduce(lambda a, b:a*b,nums)
print(product)
