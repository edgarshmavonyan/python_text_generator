import numpy as np


class MarkovVertex:
    """A vertex of a markov chain"""
    def __init__(self, current_word='end', neighbours=None):
        if neighbours is None:
            neighbours = dict()

        self.__word = current_word
        self.__next_words = list(neighbours.keys())

        total = sum(neighbours.values())
        self.__probabilities = np.array([x / total for x in neighbours.values()])

    @property
    def word(self):
        return self.__word

    @property
    def next_words(self):
        return self.__next_words

    @property
    def probabilities(self):
        return self.__probabilities

    def __str__(self):
        return self.__word
    
    def get_next(self):
        return np.random.choice(self.__next_words, 1, p=self.__probabilities)[0]
