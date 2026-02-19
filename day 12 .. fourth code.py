def reverse_numbers(n):
    if n==0:
        return
    print(n)
    reverse_numbers(n-1)

reverse_numbers(5)
