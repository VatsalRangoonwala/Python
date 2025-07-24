# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not 
# present, a message without exiting the program must be printed prompting the same.

try:
    with open("1.txt", "r") as f:
        content = f.read()
        print(content)
    with open("2.txt", "r") as f:
        content = f.read()
        print(content)
    with open("3.txt", "r") as f:
        content = f.read()
        print(content)

except Exception as e:
    print(e)