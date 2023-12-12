import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))


    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess

            self.num_letters -= 1

    def ask_for_input(self):
        while True:
            print(f"Word to Guess: {' '.join(self.word_guessed)}")
            print(f"Lives left: {self.num_lives}")
            guess = input("Please enter a single letter: ")
            

            if not (guess.isalpha() and len(guess) == 1):
                print("Invalid letter, please enter a single character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

if __name__ == "__main__":
    word_list = ["apple", "orange", "banana", "mango", "blueberry"]
    hangman_game = Hangman(word_list)
    
    print("Hangman Game Initialized:")
    print(f"Word to Guess: {' '.join(hangman_game.word_guessed)}")
    print(f"Number of Lives: {hangman_game.num_lives}")
    print(f"Number of Unique Letters: {hangman_game.num_letters}")
    print(f"List of Guesses: {hangman_game.list_of_guesses}")

hangman_game.ask_for_input()
    


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0: 
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print ("Congratulations. You won the game!")
            break

if __name__ == "__main__":
    word_list = ["apple", "orange", "banana", "mango", "blueberry"]
    print("Hangman Game initialised: ")
    play_game(word_list)

