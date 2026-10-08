Email = input("Please enter your eamil: ")

#index = Email.index("@")

#Username = Email[:index]
#Domain = Email[index + 1:]

Username = Email[:Email.index("@")]
Domain = Email[Email.index("@") + 1:]

print(f"Your username is {Username} and your domain is {Domain}")