f = open("log.txt", "r")
lines = f.readlines()
f.close()

for i in range(len(lines)):
    if "python" in lines[i].lower():
        print("Found in line", i + 1)