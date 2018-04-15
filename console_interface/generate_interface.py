"""Argument parser for generate.py"""
import argparse


def parse_args_for_generate():
    """Parses arguments for generate.py"""
    parser = argparse.ArgumentParser(description='Parse arguments for generate.py')
    parser.add_argument('--model', default='model.pickle',
                        help='path where model is located (default: model.pickle)')
    parser.add_argument('--seed',
                        help=' word, text should start with (default: randomly)')
    parser.add_argument('--length', type=int, default=20,
                        help='the length of generated text (default: 20)')
    parser.add_argument('--output',
                        help='path where generated text should be placed (default: stdout)')
    return parser.parse_args()
