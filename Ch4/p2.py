# Write a program to accept marks of 6 students and display them in a sorted manner.

print("\tSorted students marks")
a = []
b = int(input("Enter student 1 marks : "))
a.append(b)
b = int(input("Enter student 2 marks : "))
a.append(b)
b = int(input("Enter student 3 marks : "))
a.append(b)
b = int(input("Enter student 4 marks : "))
a.append(b)
b = int(input("Enter student 5 marks : "))
a.append(b)
b = int(input("Enter student 6 marks : "))
a.append(b)

a.sort()
print("Sorted in ascending order :",a)