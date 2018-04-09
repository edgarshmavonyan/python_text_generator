"""Argument parser for train.py"""
import argparse


def parse_args_for_train():
    """Parses arguments for train.py"""
    parser = argparse.ArgumentParser(description='Parse arguments for train.py')
    parser.add_argument('--input-dir',
                        help='path to location with documents for training (default: stdin)')
    parser.add_argument('--model', default='model.pickle',
                        help='path to a file where to dump model (default: model.pickle)')
    parser.add_argument('--lc', action='store_true',
                        help='flag whether to make text lowercase or not (default: false)')
    return parser.parse_args()
