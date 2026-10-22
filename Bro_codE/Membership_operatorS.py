#word = "Watermelon"

#letter = input("Guess a letter in the word: ")

#if letter in word:
#   print(f"There is a {letter}")
#else:
#   print(f"{letter} was not found")

#students = {"Fred", "James", "Jeffery"}

#student = input("Enter the name of a student: ")

#if student in students:
#   print(f"{student} is in this class")
#else:
#   print(f"{student} is NOT in this class")   

grades = {
   "Fred": 'A',
   "Jeffery": 'B',
   "Benard": 'C',
   "Phil": 'D'
}

student = input("Enter the name of a student: ")

if student in grades:
   print(f"{student}'s grade is {grades[student]}.")
else:
   print(f"{student} is not in the this class")   