import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a Number to Guess between 1 to {x}: "))
        if guess < random_number:
            print("Its too low, try again")
        elif guess > random_number:
            print("Its too high, try again")

    print(f"Congrats you guessed it right! it was {random_number}")


guess(10)
