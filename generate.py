from markov_chain.chain import MarkovChain
from console_interface.generate_interface import parse_args_for_generate
import pickle

if __name__ == '__main__':
    args = parse_args_for_generate()
    with open(args.model, "rb") as model:
        chain = pickle.load(model)
    print(chain.examine(args.length))
