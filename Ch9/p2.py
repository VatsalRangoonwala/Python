# The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi-score 
# whenever the game() function breaks the Hi-score.

import random
def game():
     return random.randint(0, 100)
score = game()
with open("hi-score.txt", "r") as f:
    hi_score = f.read()
    if(hi_score != ""):
        hi_score = int(hi_score)
    else:
         hi_score = 0

if(score>hi_score):
    print("🎉 New High Score!")
    with open("hi-score.txt", "w") as f:
          f.write(str(score))
else:
    print(f"Current High Score remains: {hi_score}")