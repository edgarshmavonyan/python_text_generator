from markov_chain.vertex import MarkovVertex
import numpy as np
from markov_chain import text_processing


class MarkovChain:
    def __init__(self, file_path: str, lowercase=False):
        self.__vertex_namespace = dict()
        self.__file_path = file_path
        # self.__start_words = list()
        # self.__start_prob = list()
        self.__cur_state = None
        self.__train_by_line(lowercase)

    def __train_by_line(self, lowercase=False):
        with open(self.__file_path, 'r') as file:
            # last_word = ''
            for line in file:
                cleaned_line = text_processing.process_block(line)

                if lowercase:
                    cleaned_line = [x.lower() for x in cleaned_line]

                # if len(cleaned_line) > 0:
                #     if last_word != '':
                #         cleaned_line = [last_word] + cleaned_line
                #     last_word = cleaned_line[-1]

                self.__add_line_to_chain(cleaned_line)

            for vertex in self.__vertex_namespace.values():
                vertex.lock()

    def __add_line_to_chain(self, line):
        for it in range(len(line)):
            word = line[it]
            if word not in self.__vertex_namespace:
                self.__vertex_namespace[word] = MarkovVertex(word)

            if it != len(line) - 1:
                self.__vertex_namespace[word].add_word(line[it + 1])

    @property
    def cur_state(self):
        return self.__cur_state

    def __get_start(self):
        self.__cur_state = np.random.choice(list(self.__vertex_namespace.keys()))
        return self.__cur_state

    def __get_next(self):
        self.__cur_state = self.__vertex_namespace[self.__cur_state].get_next()
        return self.__cur_state

    def examine(self, max_number=20):
        self.__get_start()
        text = str()
        len_counter = 0
        while len_counter < max_number:
            len_counter += 1
            text += self.cur_state
            if self.__get_next() is None:
                text += '. '
                self.__get_start()
            else:
                text += ' '

        return text
