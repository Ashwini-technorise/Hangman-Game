#Hangman game
import random

words = ["apple", "tiger", "chair", "plant", "robot"]
secret_word = random.choice(words)
display = ["_"] * len(secret_word)
wrong_guesses = 0
max_guesses = 6
guessed_letters = []

print("============================")
print("🎮 Welcome to Hangman Game!")
print("============================")
print("Guess the word one letter at a time.")
print("You have 6 wrong guesees allowed.\n")

#game loop
while wrong_guesses < max_guesses and "_" in display:
    print("Word: ", " ".join(display))
    guess = input("Enter a letter: ").lower()

    #check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!\n")
        continue
    guessed_letters.append(guess)

    #check if guess is correct
    if guess in secret_word:
        print("Correct guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining chances: ",max_guesses - wrong_guesses, "\n")

#final result
if "_" not in display:
    print("🎉Congratulations! You guessed the word: ", secret_word, "\n")
else:
    print("👎Game over! The correct word was: ", secret_word, "\n")