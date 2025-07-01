# Write a program to print yes when the age entered by the user is greater than or equal to 18.

print("\tEligiblity checker")
age = int(input("Enter your age : "))

if(age>=18):
    print("Yes, You are eligible for voting")
else:
    print("No, You are not eligible for voting")