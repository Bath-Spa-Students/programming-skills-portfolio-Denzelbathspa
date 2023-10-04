"""
Make a list called sandwich_orders and fill it with the names of various sandwiches. 
Then make an empty list called finished_sandwiches.

Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. 
As each sandwich is made, 

move it to the list of finished sandwiches. After all the sandwiches have been made, 
print a message listing each sandwich that was made.
"""

sandwich_orders = ["Chicken Sandwich","Tuna Sandwich","Peanut and Jelly Sandwich","Veggie Sandwich","Cheese Sandwich"]
finished_orders = []

for x in sandwich_orders:
    print("I made your "+x)
    finished_orders.append(x)
print("Sandwiches finished: ",end="")
for x in finished_orders:
    print(x+", ",end="")