
import random
alien_color = ["green","yellow","red"]
playerPoints = 0

rChoice = random.choice(alien_color)
print(rChoice)
if rChoice == "green":
    print("Player Just earned 5 points")
    playerPoints+=5