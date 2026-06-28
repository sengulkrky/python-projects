import random

number = random.randint(1, 100)

guessed = False
number_of_attempts = 0

while not guessed:
    guess = int(input("Guess a number: "))
    number_of_attempts += 1

    if guess < number:
        print("Too low!")
    elif guess >  number: 
        print("Too high")
    else:
        print(f"Correct! You guessed it in {number_of_attempts} attempts.")
        guessed = True