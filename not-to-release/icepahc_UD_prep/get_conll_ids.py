import pyconll
import os
import re

from collections import defaultdict

def centuryFromYear(year):
    return int(year) // 100 + 1

dir = '../CoNLLU'

ids = []
years = defaultdict(lambda: defaultdict(int))

for file in os.listdir(dir):
    file_year = file.split('.')[0]
    century = centuryFromYear(file_year)
    conll = pyconll.iter_from_file(os.path.join(dir, file))
    for sentence in conll:
        id = re.sub(r'\.psd', '', sentence.id)
        id = id.upper()
        id = re.sub(r'_', ',', id, 1)
        id = re.sub(r'_', '.', id, 1)
        ids.append(id)
        # year = id.split(',')[0].split('.')[0]
        # years[century][file] += 1
        for token in sentence:
            years[century][file] += 1

print(f'Total words: {len(ids)}')

for century, info in years.items():
    print(f'Century:\t{century}th')
    total_sents = 0
    for file, sent_num in info.items():
        print(f'\t{file}\t{sent_num}')
        total_sents += sent_num
    print(f'\n\tTotal sents\t{total_sents}')
