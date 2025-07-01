# Write a program to print multiplication table of n using for loops in reversed order

print("\tMultiplication table in reversed order")

n = int(input("Enter a number : "))

# for i in range(1, 11):
#     print(f"{n} X {11-i} = {n*(11-i)}")

# Loop from 10 to 1 (reverse)
for i in range(10, 0, -1):
    print(f"{n} x {i} = {n * i}")
