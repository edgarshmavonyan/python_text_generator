import re


def process_array(input_arr):
    temp = []
    for i in input_arr:
        for j in list(filter(None, re.split(r'\W+|[a-z]|[0-9]', i.lower()))):
            temp.append(j)
        temp.append('.')

    return temp