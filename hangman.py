import random

words = ["python", "apple", "coding", "computer", "game"]

word = random.choice(words)
print("DEBUG: The word is", word)

guessed_letters = []
attempts = 6

print("Welcome to Hangman!")

while attempts > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

if attempts == 0:
    print("\nGame Over!")
    print("The word was:", word)
