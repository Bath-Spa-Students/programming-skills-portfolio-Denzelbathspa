
defaultVar = "n/a"
userInput = {"Name":defaultVar,
             "Age":defaultVar,
             "Address":defaultVar,
             "P.O. box":defaultVar,
             "Favorite Games":defaultVar,
             "Food preference":defaultVar,
             "Workplace":defaultVar,
             "Previous or current Study":defaultVar,
             "Favorite car":defaultVar,
             "Relationship status":defaultVar
             }

for x in userInput:
    print("Enter your "+x+": ", end="")
    userInput.update({x:input("")})

print("==============================================")
for x in userInput:
    print(x+": "+userInput.get(x))