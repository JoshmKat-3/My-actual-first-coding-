import random

low_num = 0
high_num = 50
guesses = 0
answer = random.randint(low_num, high_num)
is_running = True

print("***** Python guessing game *****")
print(f"Select a number between {low_num} - {high_num}")

while is_running:

    guess = input("Enter a number: ")

# "isdigit()" checks that a whole number was entered
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess > high_num or guess < low_num:
            print("This guess is out of range")
            print(f"Select a number between {low_num} - {high_num}")
        elif guess > answer:
            print("too high")
        elif guess < answer:
            print("too low")
        else:
            print(f"{guess} is the correct number")
            print(f"It too you {guesses} tries")

    else:
        print("That is an inalid quess")
        print(f"Select a number between {low_num} - {high_num}")