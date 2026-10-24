
#Task4
def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)
        word = ""
        for char in secret_word:
            if char in guesses:
                word += char
            else:
                word += "_"

        print(word)

        return all(char in guesses for char in secret_word)

    return hangman_closure


secret_word = input("Enter a secret word: ").lower()

hangman = make_hangman(secret_word)

guessed = False

while not guessed:
    letter = input("Guess a letter: ").lower()
    guessed = hangman(letter)

print("You guessed the word!")
