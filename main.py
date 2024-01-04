import random

words = [
    "something",
    "whatever",
    "guess"
    ]

secret_word = random.choice(words)
done = False
tries = 0

display_word = []
for letter in secret_word:
    display_word += "_"

print(f"Welcome to the game\n Try to guess the word\n {display_word}")

while done == False:
    guess = input("Guess a letter:").lower()
    tries += 1
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter

    print(display_word)

    if "_" not in display_word:
        print("You got the word right")
        done = True
    
    elif tries == 10:
        done = True
        print(f"You couldn't guess the word in {tries} tries ")