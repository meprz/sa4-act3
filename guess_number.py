number = 10
guess = 11
print("I'm thinking of a number...")

while guess != number:
    guess = input("What number am I thinking of? (enter Q to quit) ")
    if guess.upper() == "Q":
        print(f"The number was {number}.")
        break
    elif int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        print(f"Sorry! Try again!")