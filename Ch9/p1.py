# Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’.

print("\tChecking twinkle is present in poems.txt")
f = open("poems.txt", "r")
t = f.read()
if("twinkle" in t.lower()):
    print("Yes, twinkle is present in the file")
else:
    print("No, twinkle is not present in the file")