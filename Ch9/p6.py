# Write a program to mine a log file and find out whether it contains ‘python’.

print("\tFinding python word in file")
f = open("log.txt", "r")
t = f.read()
if("python" in t.lower()):
    print("Yes, python is present in the file")
else:
    print("No, python is not present in the file")