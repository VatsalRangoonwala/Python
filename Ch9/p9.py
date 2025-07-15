# Write a program to find out whether a file is identical & matches the content of another file.

with open("log.txt", "r") as f:
    text1 =  f.read()

with open("donkey.txt", "r") as f:
    text2 =  f.read()

if(text1 == text2):
    print("File matches the content of another file")
else:
    print("File is identical")