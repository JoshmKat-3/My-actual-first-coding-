#typecasting is the process of converting a value of one data type to another

name = "Justin"
age = 23
gpa = 2.4
student = False

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

age = float(age)
print(type(age))

gpa = int(gpa)
print(gpa)

student = str(student)
print(type(student))
print(student)

age = bool(age)
print(age)

#We can use type casting to check if someone put data where we wanted

#implicit

x = 4
y = 2.0

x = x/y
print(type(x))






