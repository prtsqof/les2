import math

def my_round(n, nd):
    n=n*(10**nd)+0.41
    n = n//1
    return n/(10**nd)
print(my_round)