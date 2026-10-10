
rows = int(input("How many rows would you like to have?"))
colums = int(input("How many colums would you like to have?"))
symbol = input("Which symbol would you like to use?")



for x in range(rows):
    for y in range(colums):
        print(symbol, end = "")
    print()