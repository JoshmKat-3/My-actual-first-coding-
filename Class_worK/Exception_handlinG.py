# the 'Finally' is not mandatory in the code

test = int(input("What is your fav number?: "))

try:
    result = 10 / test
    print(round(result, 2))
except ZeroDivisionError:
    print("Error: Division by Zero")  
finally:
    print("This will always print")      
