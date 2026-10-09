principle = 0
time = 0
rate = 0


while principle <= 0:
    principle = int(input("Please enter the principle: "))
    if principle <= 0:
        print("Your Princile cannot be less than or Zero")

while time <= 0:
    time = int(input("Please enter the Time: "))
    if time <= 0:
        print("Your Time cannot be less than or Zero")

while rate <= 0:
    rate = int(input("Please enter the Rate: "))
    if rate <= 0:
        print("Your Princile cannot be less than or Zero")                

        

total = principle * pow((1 + rate/100), time)
print(f"After {time} years you will have ${total:.2f}")
