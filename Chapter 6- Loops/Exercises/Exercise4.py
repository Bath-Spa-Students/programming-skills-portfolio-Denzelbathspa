
sandwich_orders = ["Chicken Sandwich","Tuna Sandwich","Peanut and Jelly Sandwich","Veggie Sandwich","Cheese Sandwich"]
finished_orders = []

for x in sandwich_orders:
    print("I made your "+x)
    finished_orders.append(x)
print("Sandwiches finished: ",end="")
for x in finished_orders:
    print(x+", ",end="")