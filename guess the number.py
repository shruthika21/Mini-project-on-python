import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    
    print("Welcome to Guess the Number (Computer)!")
    print("I've picked a number between 1 and 100. Try to guess it.")

    attempts = 0
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break

if _name_ == "_main_":
    guess_the_number()
