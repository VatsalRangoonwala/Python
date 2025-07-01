# Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13 – year old.

def table(n):
    result = ""
    for j in range(1, 11):
        result += (f"{n} X {j} = {n*j}\n")
    return result

for i in range(2, 21):
    with open(f"Tables/table_{i}.txt", "w") as f:
        f.write(table(i))