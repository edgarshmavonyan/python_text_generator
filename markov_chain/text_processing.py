"""A file providing function to process a block of words"""
import re


def process_block(input_block):
    """Process line or other block
    :param input_block: str
        Given block of words
    :return: list of words from input_block"""

    return list(filter(None, re.split(r'\W+|[0-9]', input_block)))
