# Practice Exercises
def practice1():
    sales = float(input("Enter Sales: "))
    bonus = 0
    if sales > 50_000:
        bonus = 500
    else:
        bonus = 0

    print(f"Your Bonus: {str(bonus)}")

def practice2():
    earning = int(input("Enter Yearly Earnings: "))
    workExperience = int(input("Enter Work experience in years: "))

    if earning > 1000 and workExperience > 2:
        print("You are Eligable!")
    else:
        print("You are unqualified!!")


# Practice Selection
while True:
    choice = (input("Select practice 1-2: "))
    try:
        choice = int(choice)
        if choice <= 2:
            break
        else:
            print("Not in range!\nTry Again!")
            continue
    except:
        print("Only input integers within the given values")
        continue

if choice == 1:
    practice1()
if choice == 2:
    practice2()