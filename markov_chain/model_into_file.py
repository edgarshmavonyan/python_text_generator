from markov_chain.chain import MarkovChain
from markov_chain.text_processing import process_array
import numpy as np
import pickle

tweets = process_array(np.load('tweets.npy'))
chain = MarkovChain(tweets)
with open('chain.pickle', 'wb') as f:
    pickle.dump(chain, f)
