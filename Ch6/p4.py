# Write a program to find whether a given username contains less than 10 
# characters or not.

print("\tChecking username")

username = input("Enter username : ")

if(len(username)<10):
    print("username contains less than 10 characters")
else:
    print("username contains more than 10 characters")