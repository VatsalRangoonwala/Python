# Repeat program 4 for a list of such words to be censored.
print("\tReplacing censored words with #")
l = ["sex", "fuck", "nudes", "bad"]

with open("censored.txt", "r") as f:
    t = f.read()

for word in l:
    t = t.replace(word, "#" * len(word))

with open("censored.txt", "w") as f:
    f.write(t)

print("done")