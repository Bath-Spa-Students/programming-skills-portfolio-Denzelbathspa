
pet1 = {"Name":"Trixie","Age":"2","Breed":"Syrian Hamster","Owner's Name":"Edgar"}
pet2 = {"Name":"Aki","Age":"2","Breed":"Syrian Hamster","Owner's Name":"Robin"}
pet3 = {"Name":"Ed","Age":"1","Breed":"Syrian Hamster","Owner's Name":"Chinto"}
pet4 = {"Name":"Hash","Age":"1","Breed":"Syrian Hamster","Owner's Name":"David"}
pet5 = {"Name":"Jinji","Age":"2","Breed":"Syrian Hamster","Owner's Name":"Debby"}

pets = [pet1,pet2,pet3,pet4,pet5]

for x in pets:
    for y in x:
        print(y+": "+x.get(y))
    print("=============================")