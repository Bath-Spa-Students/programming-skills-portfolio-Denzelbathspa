
names = ["Beverly","Homer","Dane", "Jade","Thontie","Drazen","Seth","Aila","Chenier"]

print("I apologize for my message. I was not informed that the new dinner table won't arrive in time for the dinner. \nThere are only 2 sits available. I will be removing guests until I am left with 2 people.\n")

while (len(names)!=2):
    print(names.pop()+", sorry but I cannot invite you to dinner.")

print("")
for x in names:
    print(x+", You are still INVITED to the party")

del names[0]
del names[0]
print("\nEmpty the list: ",names)
