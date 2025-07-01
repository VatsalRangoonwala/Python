import random

print("\tSnake Water Gun game")
comp = random.choice([1,2,3])
# print(comp)

dict = {
    1: "water",
    2: "Snake",
    3: "Gun"
}

reversed_dict = {
    "w": 1,
    "s": 2,
    "g": 3
}

user = input("Enter your choice from w/s/g : ").lower()
num = reversed_dict[user]
print(f"You choose : {dict[num]}")
print(f"Computer choose : {dict[comp]}")
# print(num)

if(num == 1 and comp == 2):
    print("You loss")
elif(num == 1 and comp == 3):
    print("You win")
elif(num == 2 and comp == 1):
    print("You win")
elif(num == 2 and comp == 3):
    print("You loss")
elif(num == 3 and comp == 2):
    print("You win")
elif(num == 3 and comp == 1):
    print("You loss")
elif(num == comp):
    print("it's a draw")
else:
    print("Oops, You Entered something wrong")