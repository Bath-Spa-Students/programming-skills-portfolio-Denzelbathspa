import random
alien_color = ["green","yellow","red"]
playerPoints = 0

rChoice = random.choice(alien_color)
print("Player shot a "+rChoice+" alien")
if rChoice == "green":
    print("Player Just earned 5 points")
    playerPoints+=5
elif rChoice == "yellow":
    print("Player Just earned 10 points")
    playerPoints+=10
else:
    print("Player Just earned 15 points")
    playerPoints+=15