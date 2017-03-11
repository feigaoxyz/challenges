from typing import List

from data import DICTIONARY, LETTER_SCORES


def load_words(dictionary: str = None):
    """Load dictionary into a list and return list"""
    dictionary = dictionary or DICTIONARY
    # with open(dictionary) as f:
    #     for line in f:
    #         yield line
    return open(dictionary).read().splitlines()


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES.get(c, 0) for c in word.upper())


def max_word_value(words: List[str] = None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()

    return max(words, key=calc_word_value)


if __name__ == "__main__":
    pass  # run unittests to validate
