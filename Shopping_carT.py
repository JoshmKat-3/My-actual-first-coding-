
Item = input("What would you like to buy: ")
Price = float(input(f"How much do {Item} cost?: "))
Quantity = int(input(f"How many {Item} would you like: "))

Total = Price * Quantity

print(f"You have bought {Quantity} {Item}/s.")
print(f"Your bill is ${Total}")