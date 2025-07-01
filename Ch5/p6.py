# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.

print("\n\tFavorite languages of four friends")
fav_languages = {}

name1 = input("\nEnter name of friend 1 : ")
lang1 = input("Enter their favorite language : ")
fav_languages[name1] = lang1

name2 = input("\nEnter name of friend 2 : ")
lang2 = input("Enter their favorite language : ")
fav_languages[name2] = lang2

name3 = input("\nEnter name of friend 3 : ")
lang3 = input("Enter their favorite language : ")
fav_languages[name3] = lang3

name4 = input("\nEnter name of friend 4 : ")
lang4 = input("Enter their favorite language : ")
fav_languages[name4] = lang4

print("\nFavorite Languages Dictionary : ", fav_languages)