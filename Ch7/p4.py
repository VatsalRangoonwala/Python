# Write a program to find whether a given number is prime or not.

print("\tChecking the number is prime or not")
n = int(input("Enter a number : "))

for i in range(2, n):
    if(n%i == 0):
        print("Given number is not prime")
    else:
        print("Given number is prime")
    break