

import random 




def check_guess(guess, word, guessed_letters):
    guess = guess.lower()
    if guess in word: 
        print(f"Good guess! {guess} is in the word.")
    else: 
        print(f"Sorry, {guess} is not in the word. Try again!")
        guessed_letters.append(guess)

def ask_for_input(word):
    guessed_letters = []
    while True:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += ""
    
        print("word: ", display_word)
        print("Guessed letters:", guessed_letters)

        if display_word == word:
            print("Congratulations! You guessed the word: ", word)
            break

        guess = input("Please enter a single letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            guessed_letters.append(guess)
            check_guess(guess, word, guessed_letters)
        else:
            print("Oops! That is not a valid input.")



if __name__ == "__main__":
    word_list = ["apple", "orange", "banana", "mango", "blueberry"] 
    word = random.choice(word_list)
    print("Welcome to the word guessing game!")
    ask_for_input(word)

    


