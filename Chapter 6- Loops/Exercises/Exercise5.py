
sandwich_orders = ["Chicken Sandwich","Tuna Sandwich","Peanut and Jelly Sandwich","Veggie Sandwich","Cheese Sandwich"]
finished_orders = []

for x in range(3):
    sandwich_orders.append("pastrami")
print("The deli has run out of pastrami")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
for x in sandwich_orders:
    print("I made your "+x)
    finished_orders.append(x)
print("Sandwiches finished: ",end="")
for x in finished_orders:
    print(x+", ",end="")