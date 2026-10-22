
questions = ("What is 7 cubed?",
             "What is the square root of 64",
             "how many 2s are in 63?",
             "What is 250cm in meters?",
             "how many milliliters is 2.7L?")
options = (("A. 794", "B. 777", "C. 437", "D. 343"), 
           ("A. 4", "B. 2", "C. 8", "D. 32"), 
           ("A. 31", "B. 32", "C. 63", "D. 12"), 
           ("A. 2m", "B. 3m", "C. 2.5m", "D. 6.7m"), 
           ("A. 2700", "B. 27000", "C. 270", "D. 27"))

answers = ("D", "C", "A", "C", "A")
guesses = []

score = 0
question_num = 0

for question in questions:
    print("***************************************")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Do you choose A, B, C, or D : ").upper()
    guesses.append(guess)

    if guess == answers[question_num ]:
        score += 1 
        print("That is right!")
    else:
        print("That is wrong!")
        print(f"The correct answer is {answers[question_num]}")
    question_num += 1    

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("             Results               ")
print("***********************************")

print("Answers:", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses:", end=" ")
for guess in guesses:
    print(guess, end=" ")    
print()

score = float(score / len(questions)) * 100
print(f"You got: {score}%")