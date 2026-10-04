Weight = float(input("What is your weight?: "))
Unit = input("Is that Kilograms or Pounds (Kg/Lb)?: ")

if Unit == "Kg":
    Unit = "Lbs"
    Weight = Weight * 2.205
    print(f"You weigh {round(Weight, 2)}{Unit}")
elif Unit == "Lb":
    Unit = "Kgs"
    Weight = Weight / 2.205
    print(f"You weigh {round(Weight, 2)}{Unit}")
else:
    print(f"{Unit} is invaid")    

