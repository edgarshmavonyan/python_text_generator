from markov_chain.chain import MarkovChain
from markov_chain import load_and_examine as MChain
import pickle
import numpy as np

LIST = ['Тёма', 'Амир', 'Эдгар', 'полу:идол', 'Юрец', 'Лёша', 'Андрей']


def random_liver():
    return np.random.choice(LIST)


chain = MChain.load_chain()
queries = int(input())
size = int(input())
for i in range(queries):
    print(random_liver(), 'says:', MChain.examine(chain, size))
