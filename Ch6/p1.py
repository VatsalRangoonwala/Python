# Write a program to find the greatest of four numbers entered by the user.

print("\tFind greatest of four numbers")

a = int(input("Enter number : "))
b = int(input("Enter number : "))
c = int(input("Enter number : "))
d = int(input("Enter number : "))

if(a>b and a>c and a>d):
    print(f"{a} is greatest")
elif(b>a and b>c and b>d):
    print(f"{b} is greatest")
elif(c>a and c>b and c>d):
    print(f"{c} is greatest")
elif(d>a and d>b and d>c):
    print(f"{d} is greatest")
else:
    print("There are two or more same greatest numbers so greatest is not found\nplease enter all unique numbers")