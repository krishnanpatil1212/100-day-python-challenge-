from functools import reduce

nums=[10,25,40,45678]
max_num=reduce(lambda a, b: a if a>b else b,nums)
print(max_num)
