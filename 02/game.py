#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    return random.sample(POUCH, NUM_LETTERS)


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    while True:
        word = input("Gauss: ").upper()
        try:
            _validation(word, draw)
        except ValueError:
            print('!!! "{}" is not a proper word. Try again.'.format(word))
        else:
            return word


def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    if all(word.count(c) <= draw.count(c) for c in word) and word.lower() in DICTIONARY:
        return True
    else:
        raise ValueError


# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    return [w for w in _get_permutations_draw(draw) if w.lower() in DICTIONARY]


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    result = []
    for k in range(len(draw)):
        for w in itertools.permutations(draw, k + 1):
            result.append(''.join(w))
    return result


# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()