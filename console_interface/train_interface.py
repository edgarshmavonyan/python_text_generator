"""Argument parser for train.py"""
from argparse import ArgumentParser


def parse_args_for_train():
    """Parses arguments for train.py"""
    parser = ArgumentParser(description='Parse arguments for train.py')
    parser.add_argument('--input-dir',
                        help='directory with documents for train (default: stdin)')
    parser.add_argument('--model', default='model.pickle',
                        help='file where to dump model (default: model.pickle)')
    parser.add_argument('--lc', action='store_true',
                        help='flag whether to make text lowercase (default: false)')
    return parser.parse_args()
