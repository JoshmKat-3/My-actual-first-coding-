# Name = input("What is your mothers maiden name?: ")
# Phone_numbeR = input("What is your phone nummber?: ")


# Result = len(Name)
# Result = Name.find("u")
# Result = Name.rfind("a")

# Name = Name.capitalize()
# Name = Name.upper()
# Name = Name.lower()
# Result = Name.isdigit()
# Result = Name.isalpha()
# Comida =  Phone_numbeR.count("-")
# Phone_numbeR = Phone_numbeR.replace("-", "")


# print(Result)
# print(Phone_numbeR)

# Exersise

Username = input("PLease enter a username: ")

if len(Username) > 12:
    print("Username is too long.")
elif not Username.find(" ") == -1:
    print("Your username may not contain spaces")
elif not Username.isalpha():
    print("Your username may not contain numbers.")
else:
    print(f"Welcome {Username}.")    


