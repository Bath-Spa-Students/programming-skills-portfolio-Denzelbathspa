
exitN = 0
while True:
    try:
        age = int(input("Goodmorning sir/ma'am may I have your age: "))
        if age < 3 and age >= 1:
            print("Your ticket will be $3. Thank you")
            exitN=0
        if age >= 3 and age <= 12:
            print("Your ticket will be $10. Thank you")
            exitN=0
        if age > 12:
            print("Your ticket will be $15. Thank you")
            exitN=0
    except:
        print("Please put a number!!")
        print("To EXIT type any letter again.")
        if exitN == 1:
            print("YOU HAVE EXITED THE PROGRAM!!")
            break
        exitN+=1
