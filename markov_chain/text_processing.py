import re


def process_block(input_block):
    return list(filter(None, re.split(r'\W+|[0-9]', input_block)))
