# Write a program to wipe out the content of a file using python
def delete_file_content(name):
    with open(name, "w") as f:
        f.write("")

delete_file_content("poems.txt")