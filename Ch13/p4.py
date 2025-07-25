# Write a program to filter a list of numbers which are divisible by 5.

l = [1,2,3,4,45,6,7,7,8,9,55,88,50,35,2,5,45]

def divisibleBy5(i):
    return i%5 == 0
    
new = filter(divisibleBy5, l)
print(list(new))