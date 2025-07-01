# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

hindi_dict = {
    "roti" : "bread",
    "kutta" : "dog",
    "billi" : "cat",
    "makan" : "house",
    "kapada" : "clothes"
}

print("\tHindi to english dictionary")
print("Available Hindi words :", ', '.join(hindi_dict.keys()))
a = input("Enter any word from above to traslate : ")
print(f"English traslation of '{a}' is : {hindi_dict[a]}")