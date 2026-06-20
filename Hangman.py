import random

words = ["python", "apple", "java", "cloud", "coding"]
word = random.choice(words)

guessed = []
attempts = 6

print("=== HANGMAN GAME ===")

while attempts > 0:
    display = ""

    for ch in word:
        if ch in guessed:
            display += ch + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("🎉 You Won!")
        break

    guess = input("Enter letter: ").lower()

    if guess in guessed:
        print("Already guessed")
        continue

    guessed.append(guess)

    if guess not in word:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print("Game Over")
    print("Word was:", word)
