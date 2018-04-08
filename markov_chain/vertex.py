import numpy as np


class MarkovVertex:
    """A vertex of a markov chain"""
    def __init__(self, current_word):
        self.__word = current_word
        self.__regime = False
        self.__next_words = list()
        self.__probabilities = list()
        self.__next_words_dict = dict()

    def __str__(self):
        return self.__word

    def add_word(self, word: str):
        if self.__regime:
            raise BaseException
        if word in self.__next_words_dict:
            self.__next_words_dict[word] += 1
        else:
            self.__next_words_dict[word] = 1

    def lock(self):
        self.__regime = True
        self.__next_words = list(self.__next_words_dict.keys())
        total = sum(self.__next_words_dict.values())
        self.__probabilities = [x / total for x in self.__next_words_dict.values()]
        del self.__next_words_dict
        del total

    @property
    def next_words(self):
        return self.__next_words

    @property
    def probabilities(self):
        return self.__probabilities

    def get_next(self):
        if len(self.__next_words) == 0:
            return None
        return np.random.choice(self.__next_words, p=self.__probabilities)
