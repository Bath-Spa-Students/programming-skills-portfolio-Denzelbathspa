
pizza = ""
while True:
    toppings = input("Goodmorning sir/ma'am, what toppings would like to have on your pizza?: ")
    if toppings.lower() == "quit":
        break
    pizza+=toppings+", "
print("Your pizza toppings are "+pizza+"\nThank you for ordering!!")