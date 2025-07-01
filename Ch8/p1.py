# Write a program using functions to find greatest of three numbers.

print("\tFind greatest of 3 numbers")

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    else:
        print("Please Enter all unique numbers")

n1 = int(input("Enter 1st number : "))
n2 = int(input("Enter 2nd number : "))
n3 = int(input("Enter 3rd number : "))

result = greatest(n1, n2, n3)

print(f"Greatest is : {result}")