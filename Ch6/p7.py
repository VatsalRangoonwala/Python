# Write a program to find out whether a given post is talking about “Harry” or not.

print("\tPost information")
post = input("Give your post here : ")

if("harry" in post.lower()):
    print("given post is talking about Harry")
else:
    print("given post is not talking about Harry")