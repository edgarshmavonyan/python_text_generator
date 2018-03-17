from markov_chain.chain import MarkovChain
from markov_chain import load_and_examine as MChain
import pickle
import numpy as np

chain = MChain.load_chain()
queries = int(input())
for i in range(queries):
    print(chain.examine())
