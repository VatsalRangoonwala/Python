# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.

print("\tFind Student Result")

s1 = int(input("Enter marks of physics : "))
s2 = int(input("Enter marks of chemistry : "))
s3 = int(input("Enter marks of maths : "))

total = (s1 + s2 + s3)/3

if(s1>=33 and s2>=33 and s3>=33 and total>=40):
    print(f"Congratulations, you are PASS with {total}%")
else:
    print("You are FAIL, Try again next year")