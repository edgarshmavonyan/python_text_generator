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
        """Cur state getter"""
        return self.__cur_state

    def __get_start(self, seed=None):
        """Start word getter
        :param seed: str
            A word to start (chosen randomly, if None)"""
        if seed is None:
            self.__cur_state = np.random.choice(list(self.__vertex_namespace.keys()))
            return self.__cur_state
        else:
            self.__cur_state = seed
            return seed

    def __get_next(self):
        """Get next state of the chain"""
        if self.__cur_state is not in self.__vertex_namespace:
            return None

        self.__cur_state = self.__vertex_namespace[self.__cur_state].get_next()
        return self.__cur_state

    def generate(self, stream, start_word, length):
        """Generate text and print into the stream
        :param stream
            An output stream
        :param start_word
            The word to start
        :param length: int
            A number of words in generated text"""

        self.__get_start(start_word)
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
        """Generate method runner
        :param output_file
            The file where we write (stdout, if None)
        :param start_word: str
            The word, the text we start from (chosen randomly, if None)
        :param length: int
            The length of generated text (default: 20)"""

        if output_file is None:
            self.generate(sys.stdout, start_word, length)
        else:
            with open(output_file, 'w') as stream:
                self.generate(stream, start_word, length)
