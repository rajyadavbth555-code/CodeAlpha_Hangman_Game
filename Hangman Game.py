import random

def play_hangman():
    # 1. LIST & STRINGS: A small predefined list of 5 words
    word_list = ["python", "hangman", "coding", "simple", "random"]

    # 2. RANDOM: Select a random word from the list
    secret_word = random.choice(word_list).upper()

    # Track game state using lists and integers
    guessed_letters = []
    word_display = ["_" for _ in secret_word]
    incorrect_guesses = 0
    max_incorrect = 6

    print("--- Welcome to Hangman! ---")
    print("Guess the secret word one letter at a time.")

    # 3. WHILE LOOP: Continue until max incorrect guesses reached OR word is solved
    while incorrect_guesses < max_incorrect and "_" in word_display:
        print("\n" + "=" * 30)
        print(f"Word: {' '.join(word_display)}")
        print(f"Incorrect guesses remaining: {max_incorrect - incorrect_guesses}")
        print(
            f"Letters guessed: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}"
        )

        # Get user input
        guess = input("Enter a letter: ").strip().upper()

        # 4. IF-ELSE: Validate input (single alphabetical character)
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        # Check for repeated guesses
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.append(guess)

        # Check if the guessed letter is in the secret word
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            # Update the display list where the letter matches
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    word_display[index] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

    # Game Over - Check win or lose condition
    print("\n" + "=" * 30)
    if "_" not in word_display:
        print(f"Congratulations! You guessed the word: {secret_word}")
    else:
        print(f"Game Over! You ran out of guesses. The word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()