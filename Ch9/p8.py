# Write a program to make a copy of a text file “this. txt”

with open("log.txt", "r") as f:
    text =  f.read()

with open("copy_log.txt", "w") as f:
    f.write(text)

print("copied")