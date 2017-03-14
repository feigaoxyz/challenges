import sys
from string import ascii_lowercase

from graphics import hang_graphics
from movies import get_movie as get_word  # keep interface generic

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'


class Hangman(object):
    def __init__(self, word):
        self.guessed: set = set()
        self.word: str = word
        self.error: int = 0

    def run(self):
        while True:
            print(HANG_GRAPHICS[self.error])
            guessed_word = self.str_mask()
            print('\n' + ' '.join(guessed_word))
            if self.error == ALLOWED_GUESSES - 1:
                print("You LOSE!!!")
                print("The asnwer was: " + self.word)
                break
            if guessed_word == self.word:
                print("You WIN!!!")
                break

            guess = self.prompt_guess()
            self.update_guess(guess)

    def prompt_guess(self):
        while True:
            guess_raw = input("Make your {} of {} guess: ".format(self.error + 1, ALLOWED_GUESSES))
            guess = [c for c in guess_raw.lower() if c in ASCII and c not in self.guessed]
            if guess:
                return guess

    def update_guess(self, guess):
        self.guessed.update(set(guess))
        self.error = min(ALLOWED_GUESSES - 1,
                         sum(c not in self.word.lower() for c in self.guessed))

    def str_mask(self):
        return ''.join(c if c.lower() in self.guessed or c.lower() not in ASCII
                       else PLACEHOLDER
                       for c in word)


# or use functions ...


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()
    print(word)

    # init / call program
    Hangman(word).run()
