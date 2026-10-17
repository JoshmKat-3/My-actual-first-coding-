import random

low = 0
high = 50
guesses = 0

number = random.randint(low, high)

while True:
    guess = int(input(f"Guess a number between {low} - {high}: "))
    guesses += 1

    if guess > number:
        print("too high")
    elif guess < number:
        print("too low")
    else:
        print(f"{guess} is the corect number")
        break

print(f"It took you {guesses} tries")
