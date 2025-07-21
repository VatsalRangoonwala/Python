# We are going to write a program that generates a random number and asks the user to guess it.

import random

number = random.randint(1, 100)
attempts = 0
ans = 0

print("\tTHE PERFECT GUESS")
print("\nGuess the number between 1 to 100")
while(ans != number):
    ans = int(input("Enter the number: "))

    if(ans > number):
        print("Lower number please")
    elif(ans < number):
        print("Higher number please")
    attempts += 1

print("\tCongratulations! You Win")
print(f"You guessed the correct number {number} in {attempts} attempts")