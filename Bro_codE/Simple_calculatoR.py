operator = input("please choose an operator ( +, -, *, /): ")

num1 = float(input("PLease enter a number: "))
num2 = float(input("PLease enter a number: "))

if operator == "+":
    result = (num1 + num2)
    print(round(result, 2))
elif operator == "-":
    result = (num1 - num2)
    print(round(result, 2))
elif operator == "*":
    result = (num1 * num2)
    print(round(result, 2))  
elif operator == "/":
    result = (num1 / num2)
    print(round(result, 2))  
else:
    print(f"{operator} is not a valid operator")        

   