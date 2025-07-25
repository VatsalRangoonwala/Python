# Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

l = [1,2,3,34,5,6,70000,8,9,9,98,766,654]

def max(a,b):
    if(a>b):
        return a
    return b

r = reduce(max, l)
print(r)