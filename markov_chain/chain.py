"""Markov chain bigrams implementation"""
from markov_chain.vertex import MarkovVertex
import numpy as np
import sys
from markov_chain import text_processing
from os import path
from os import listdir


class MarkovChain:
    """Class representing markov chain"""
    def __init__(self, input_dir: str, lowercase=False):
        """Constructor
        :param input_dir: str
            The folder with text collection (stdin, if None)
        :param lowercase: bool
            Boolean, saying if we need to make all words lowercase"""

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
        """Add file to the chain by line
        :param file
            A file to read(stdint, if None)
        :param lowercase: bool
            Boolean, saying if we need to make all words lowercase"""

        for line in file:
            cleaned_line = text_processing.process_block(line)

            if lowercase:
                cleaned_line = [x.lower() for x in cleaned_line]

            self.__add_line_to_chain(cleaned_line)

    def __add_line_to_chain(self, line):
        """Add cleaned line to chain
        :param line: list
            A list of words in the line"""
        for it in range(len(line)):
            word = line[it]
            if word not in self.__vertex_namespace:
                self.__vertex_namespace[word] = MarkovVertex(word)

            if it != len(line) - 1:
                self.__vertex_namespace[word].add_word(line[it + 1])

    @property
    def cur_state(self):
        """Cur state getter
        :return: string with current state"""
        return self.__cur_state

    def __get_start(self, seed=None):
        """Start word getter
        :param seed: str
            A word to start (chosen randomly, if None)
        :return: string with start word"""
        if seed is None:
            self.__cur_state = \
                np.random.choice(list(self.__vertex_namespace.keys()))

            return self.__cur_state
        else:
            self.__cur_state = seed
            return seed

    def __get_next(self):
        """Get next state of the chain:
        :return: next state in string"""
        if self.__cur_state not in self.__vertex_namespace:
            return None

        self.__cur_state = self.__vertex_namespace[self.__cur_state].get_next()
        return self.__cur_state

    def generate(self, stream, start_word, line_length, length):
        """Generate text and print into the stream
        :param stream
            An output stream (stdout, if None)
        :param start_word
            The word to start (randomly, if None)
        :param line_length
            Length of a generated line (default: 100)
        :param length: int
            A number of words in generated text (default: 20)"""

        self.__get_start(start_word)
        text = str()

        for len_counter in range(1, length + 1):
            text += self.cur_state
            if self.__get_next() is None:
                text += '. '
                self.__get_start()
            else:
                text += ' '
            if len_counter % line_length == 0 and len_counter != length:
                print(text, file=stream)
                text = str()

        if text != '':
            print(text + '.', file=stream)

    def examine(self, output_file, start_word, line_length, length):
        """Generate method runner
        :param output_file
            The file where we write (stdout, if None)
        :param start_word: str
            The word, the text we start from (chosen randomly, if None)
        :param line_length: int
            The length of a generated line (default: 100)
        :param length: int
            The length of generated text (default: 20)"""

        if output_file is None:
            self.generate(sys.stdout, start_word, line_length, length)
        else:
            with open(output_file, 'w') as stream:
                self.generate(stream, start_word, line_length, length)
