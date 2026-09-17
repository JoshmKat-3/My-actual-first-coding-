import math

a = float(input("Enter the length of side A: "))
b = float(input("Enter the length of side B: "))

c = math.sqrt(a ** 2 + b ** 2)
#alernatively, 
#c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The length of the hypotenus is: {round(c, 2)}cm")