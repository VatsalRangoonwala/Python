# Write a program which finds out whether a given name is present in a list or not.

print("\tChecking the name is in list or not")
l = ["Yash", "Vatsal", "Jyot", "Megh", "Ayush", "Dipen", "Parth", "Urja", "Kashish"]
name = input("Enter your name properly : ")
if(name in l):
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")