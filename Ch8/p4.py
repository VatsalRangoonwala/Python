# Write a recursive function to calculate the sum of first n natural numbers.

print("\tSum of n natural numbers using recursion")

def sum(n):
    if(n==1):
        return 1
    else:
        return n + sum(n-1)
    
num = int(input("Enter the number : "))
result = sum(num)
print(f"Sum of {num} natural numbers is : {result}")