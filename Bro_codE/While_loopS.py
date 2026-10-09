#Name = input("Please enter your name: ")

#while Name == "":
#    print("You have not entered your name")
#    Name = input("Please enter your name: ")
#else:
#    print(f"Welcome {Name}") 

#Age = int(input("How old are you: "))

#while Age < 0:
#    print("Age cannot be negative.")
#    Age = int(input("PLease enter the correct age"))
#else:
#    print(f"You are {Age} years old") 

food = input("What is your favorite food (Press q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("What other food do you like (Press q to quit): ")

print("see ya")    