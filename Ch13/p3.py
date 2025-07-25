# A list contains the multiplication table of 7. write a program to convert it to vertical 
# string of same numbers.

l = [str(i*7) for i in range(1, 11)]
newL = "\n".join(l)
print(newL)