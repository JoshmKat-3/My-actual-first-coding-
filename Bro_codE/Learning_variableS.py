first_name = "Josh"
food = "Burgers"
email = "Joshuatheprogrammer@doesntexist.com"

#These are strings
print(f"Wassup {first_name}")
print(f"Do you like {food}?")      
print(f"BTW your email is {email}")

#These are integers
#Do not put in any type o f quotes otherwise itll become a string
age = 25
quantity = 15
num_of_learners = 12

print(f"How are you only {age} years old?")
print(f"Your are buying {quantity} fishes")
print(f"There are {num_of_learners} learners in your class")

#These are floats
price = 12.99
gpa = 3.9
distance = 6.7 

print(f"Each fish costs ${price}")
print(f"Unfortunately, your GPA is: {gpa}")
print(f"You ran a distance of {distance} km")

#These are booleans
# Starts with capital letter

is_hungry = False

print(f"Are you hungry Josh? {is_hungry}")

if is_hungry:
    print("lets get some burger")
else:
 print("okay lets go to the park then")
