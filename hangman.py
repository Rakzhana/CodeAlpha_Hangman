import random

def choose_word():
    """Returns a random word from a predefined list."""
    words = ["mango","school", "friend",
    "family", "mountain", "forest",
    "happy", "laugh", "dream", "hope",
    "music","travel", "sunshine",  "winter"]
    return random.choice(words)


def display_progress(word, guessed_letters):
    """Displays the current progress of the guessed word."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("🎮 Welcome to Hangman!")
    print("You have 6 incorrect guesses.\n")

    while attempts > 0:
        print("Word:", display_progress(word, guessed_letters))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word correctly.")
            return

        guess = input("Enter a letter: ").lower()

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠ Enter only one alphabetic character.\n")
            continue

        if guess in guessed_letters:
            print("⚠ You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Good guess!\n")
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}\n")

    print("💀 Game Over!")
    print("The correct word was:", word)


# Run the game
hangman()

