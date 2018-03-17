import pandas as pd
import numpy as np
import pickle

data_set = pd.read_csv('positive2.csv', error_bad_lines=False, sep=';')
needed = [data_set['Tweet'].iloc[i] for i in range(len(data_set))]
np.save('tweets', needed)