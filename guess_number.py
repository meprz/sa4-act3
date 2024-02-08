number = 10
guess = 11
num_guesses = 3
print("I'm thinking of a number...")

while guess != number and num_guesses > 0:
    guess = input("What number am I thinking of? (enter Q to quit) ")
    if guess.upper() == "Q":
        print(f"The number was {number}.")
        break
    elif int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        num_guesses -= 1
        if int(guess) > number:
            print("Your guess was too high.")
        else:
            print("Your guess was too low.")
        if num_guesses > 0:
            print(f"Sorry! Try again! (# of guesses remaining: {num_guesses})")
        else:
            print(f"Sorry! The number was {number}.")