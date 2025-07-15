# A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file

with open("donkey.txt", "r") as f:
    t = f.read()

# print(len("donkey"))

    new_t = t.replace("donkey", "#" * len("donkey"))

with open("donkey.txt", "w") as f:
    f.write(new_t)

print("done")