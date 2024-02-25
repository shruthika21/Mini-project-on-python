import random

def choose_word():
    # List of words for the game
    words = ["apple", "banana", "orange", "grape", "pineapple", "watermelon", "strawberry", "blueberry", "kiwi"]
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with dashes for unguessed letters
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "-"
    return displayed_word

def hangman():
    print("Welcome to Hangman!")

    # Choose a word
    word = choose_word()
    word_length = len(word)

    # Initialize variables
    attempts = 6
    guessed_letters = []

    # Main game loop
    while True:
        # Display word with dashes for unguessed letters
        print(display_word(word, guessed_letters))

        # Check if player has won
        if "-" not in display_word(word, guessed_letters):
            print("Congratulations! You've guessed the word:", word)
            break

        # Prompt user for guess
        guess = input("Guess a letter: ").lower()

        # Check if guess is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        # Add letter to guessed letters
        guessed_letters.append(guess)

        # Check if guess is in the word
        if guess not in word:
            attempts -= 1
            print("Incorrect guess. Attempts left:", attempts)
            if attempts == 0:
                print("Sorry, you've run out of attempts. The word was:", word)
                break

if _name_ == "_main_":
    hangman()
