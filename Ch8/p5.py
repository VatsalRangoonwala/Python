# Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

print("\tRevers triangle pattern")

def pattern(n):
    for i in range(n):
        print("*" * (n-i))

num = int(input("Enter a number : "))
pattern(num)