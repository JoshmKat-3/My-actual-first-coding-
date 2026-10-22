Weight = float(input("What is your weight?: "))
Unit = input("Is that Kilograms or Pounds (Kg/Lb)?: ")

# Lb --> Kg
if Unit == "Kg":
    Unit = "Lbs"
    Weight = Weight * 2.205
    print(f"You weigh {round(Weight, 2)}{Unit}")

# Kg --> Lb
elif Unit == "Lb":
    Unit = "Kgs"
    Weight = Weight / 2.205
    print(f"You weigh {round(Weight, 2)}{Unit}")

#Anything else is invalid
else:
    print(f"{Unit} is invaid")    

