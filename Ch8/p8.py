# Write a python function to print multiplication table of a given number.

print("\tMultiplication Table Using Function")

def table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

num = int(input("Enter the number : "))
table(num)