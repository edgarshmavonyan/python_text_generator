from markov_chain.chain import MarkovChain
import pickle


def load_chain():
    with open('markov_chain/chain.pickle', 'rb') as f:
        loaded_chain = pickle.load(f)
    return loaded_chain


def examine(chain: MarkovChain, max_number: int):
    text = chain.get_start() + ' '
    len_counter = 0
    while chain.get_next() is not None and len_counter < max_number:
        len_counter += 1
        text += chain.cur_state + ' '

    return text
