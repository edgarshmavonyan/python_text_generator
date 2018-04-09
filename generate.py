"""Generates text"""
from console_interface.generate_interface import parse_args_for_generate
import pickle


def generate_text(args):
    """Generates the text
    :param args: Namespace
        Namespace with command args"""

    with open(args.model, "rb") as model:
        chain = pickle.load(model)
    chain.examine(args.output, args.length)


def main():
    args = parse_args_for_generate()
    generate_text(args)


if __name__ == '__main__':
    main()
