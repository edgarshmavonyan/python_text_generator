"""Argument parser for generate.py"""
from argparse import ArgumentParser

DEFAULT_LINE_LENGTH = 100
DEFAULT_TEXT_LENGTH = 20


def parse_args_for_generate():
    """Parses arguments for generate.py
    :return: parser with required arguments"""
    parser = ArgumentParser(description='Parse arguments for generate.py')
    parser.add_argument('--model', default='model.pickle',
                        help='path where model is located\
                         (default: model.pickle)')
    parser.add_argument('--seed',
                        help=' word, text should start with\
                        (default: randomly)')

    parser.add_argument('--length', type=int, default=DEFAULT_TEXT_LENGTH,
                        help='the length of generated text (default: 20)')

    parser.add_argument('--output',
                        help='path where generated text should be placed\
                        (default: stdout)')

    parser.add_argument('--line-length',
                        type=int, default=DEFAULT_LINE_LENGTH,
                        help='length of a generated line\
                        (default: 100)')

    return parser.parse_args()
