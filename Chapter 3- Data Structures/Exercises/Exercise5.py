
names = ["Beverly","Homer","Dane"]
message = [", please go to dinner with us. Love you always", ", I would like to invite you to dinner. Please join with us.",", you are invited to dinner please come with us!"]

count = 0
for x,y in zip(names,message):
    if x == "Dane":
        print(x+" cannot come to Dinner.")
        names[count]="Lolo Edward"
        print("Lolo Edward"+y)
    else:
        print(x+y)
    count+=1