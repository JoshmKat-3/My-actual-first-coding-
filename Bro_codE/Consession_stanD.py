menu = {"popcorn": 50,
        "chocolate": 30,
        "slushi": 40,
        "soda": 15,
        "water": 10,
        "chips": 20
        }

cart = []
total = 0

print("------------ MENU-----------")
for key, value in menu.items():
    print(f"{key:5}:${value}")
print("****************************")    

while True:
    food = input("What would you like to buy (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("***************** YOUR ORDER ****************")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Your total is: ${total}")