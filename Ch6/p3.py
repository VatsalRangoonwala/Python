# A spam comment is defined as a text containing following keywords:
# "Make a lot of money", "buy now", "subscribe this", "click this". Write a program 
# to detect these spams.

print("\tSpam detector")

spam1 = "make a lot of money" 
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click this"

comment = input("Enter comment here : ")
if((spam4 or spam1 or spam2 or spam3) in comment.lower()):
    print("This is a spam comment")
else:
    print("This is not a spam comment")