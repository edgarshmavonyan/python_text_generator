from markov_chain.chain import MarkovChain
from console_interface.train_interface import parse_args_for_train
import pickle


if __name__ == '__main__':
    args = parse_args_for_train()
    chain = MarkovChain(args.input_dir, lowercase=args.lc)
    with open(args.model, 'wb') as file:
        pickle.dump(chain, file)
