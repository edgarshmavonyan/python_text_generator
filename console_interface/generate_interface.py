import argparse


def parse_args_for_generate():
    parser = argparse.ArgumentParser(description='Parse arguments for generate.py')
    parser.add_argument('--model', default='model.pickle',
                        help='path where trained model is located (default: model.pickle)')
    parser.add_argument('--seed',
                        help='the word the text should start with (default: chosen randomly)')
    parser.add_argument('--length', type=int, default=20,
                        help='the length of generated text (default: 20)')
    parser.add_argument('--output',
                        help='path where the generated text should be placed (default: stdout)')
    return parser.parse_args()
