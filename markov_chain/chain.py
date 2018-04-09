from markov_chain.vertex import MarkovVertex
import numpy as np
import sys
from markov_chain import text_processing
from os import path
from os import listdir


class MarkovChain:
    def __init__(self, input_dir: str, lowercase=False):
        self.__vertex_namespace = dict()
        if input_dir is None:
            self.__train_by_line(sys.stdin, lowercase)
        else:
            for file_path in listdir(input_dir):

                with open(path.join(input_dir, file_path),
                          encoding='UTF-8') as file:

                    self.__train_by_line(file, lowercase)

        for vertex in self.__vertex_namespace.values():
            vertex.lock()

        self.__cur_state = None

    def __train_by_line(self, file, lowercase=False):
        for line in file:
            cleaned_line = text_processing.process_block(line)

            if lowercase:
                cleaned_line = [x.lower() for x in cleaned_line]

            self.__add_line_to_chain(cleaned_line)

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

    def generate(self, stream, length):
        self.__get_start()
        text = str()
        len_counter = 0
        while len_counter < length:
            len_counter += 1
            text += self.cur_state
            if self.__get_next() is None:
                text += '. '
                self.__get_start()
            else:
                text += ' '
            if len_counter % 100 == 0:
                print(text, file=stream)
                text = str()

        if text != '':
            print(text, file=stream)

    def examine(self, output_file, start_word, length=20):
        if output_file is None:
            self.generate(sys.stdout, length)
        else:
            with open(output_file, 'w') as stream:
                self.generate(stream, length)
