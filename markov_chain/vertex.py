"""Implementation of vertex of markov chain"""
import numpy as np
from collections import defaultdict


class MarkovVertex:
    """A vertex of a markov chain"""
    def __init__(self, current_word):
        """Constructor
        :param current_word: str
            The word, which is represented by this vertex"""

        self.__word = current_word
        self.__regime = False
        self.__next_words = list()
        self.__probabilities = list()
        self.__next_words_dict = defaultdict(int)

    def __str__(self):
        """Convenient output
        :return: current state in string"""
        return self.__word

    def add_word(self, word: str):
        """Add next word to vertex
        :param word: str
            A word, which occured after current in text"""

        if self.__regime:
            raise BaseException

        self.__next_words_dict[word] += 1

    def lock(self):
        """Lock vertex to calculate probabilities"""
        self.__regime = True
        self.__next_words = list(self.__next_words_dict.keys())
        total = sum(self.__next_words_dict.values())

        self.__probabilities = \
            [x / total for x in self.__next_words_dict.values()]

        del self.__next_words_dict
        del total

    def get_next(self):
        """A method to get next state of chain randomly
        :return: chosen randomly next state of a chain in string"""
        if len(self.__next_words) == 0:
            return None
        return np.random.choice(self.__next_words, p=self.__probabilities)
