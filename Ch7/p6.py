# Write a program to calculate the factorial of a given number using for loop.

print("\tFind Factorial")
n = int(input("Enter a number : "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(f"Factorial of {n} is : {fact}")