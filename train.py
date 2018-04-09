from markov_chain.chain import MarkovChain
from console_interface.train_interface import parse_args_for_train
import pickle


def train_and_dump(arguments):
    chain = MarkovChain(arguments.input_dir, lowercase=arguments.lc)
    with open(arguments.model, 'wb') as file:
        pickle.dump(chain, file)


def main():
    args = parse_args_for_train()
    train_and_dump(args)


if __name__ == '__main__':
    main()
