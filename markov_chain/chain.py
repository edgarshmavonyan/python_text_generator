from markov_chain.vertex import MarkovVertex
import numpy as np
from markov_chain.text_processing import process_array


class MarkovChain:
    def __init__(self, text):
        self.__namespace = dict()
        self.__start_words = list()
        self.__start_prob = list()
        self.__cur_state = None
        self.__build_from_text(text)

    def __build_from_text(self, text):
        word_dict = dict()
        start_dict = dict()
        for i in range(len(text)):
            word = text[i]
            if word not in word_dict:
                word_dict[word] = dict()
            if word != '.':
                start_dict[word] = start_dict.get(word, 0) + 1
                if i < len(text) - 1:
                    word_dict[word][text[i + 1]] = word_dict[word].get(text[i + 1], 0) + 1

        for items in word_dict.items():
            self.__namespace[items[0]] = MarkovVertex(items[0], items[1])
        del word_dict

        self.__start_words = list(start_dict.keys())
        total = sum(start_dict.values())
        self.__start_prob = [x / total for x in start_dict.values()]
        del start_dict

    @property
    def cur_state(self):
        return self.__cur_state

    def __get_start(self):
        self.__cur_state = np.random.choice(self.__start_words, p=self.__start_prob)
        return self.__cur_state

    def __get_next(self):
        self.__cur_state = self.__namespace[self.__cur_state].get_next()
        return self.__cur_state

    def examine(self, max_number=20):
        text = self.__get_start() + ' '
        len_counter = 0
        while self.__get_next() is not None and len_counter < max_number:
            len_counter += 1
            text += self.cur_state + ' '

        return text
