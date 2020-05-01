import pyconll
import os
import re


dir = '../../CoNLLU_bkp'

error_sent_ids = []

for file in os.listdir(dir):
    conll = pyconll.iter_from_file(os.path.join(dir, file))
    for sentence in conll:
        count_roots = 0
        for token in sentence:
            if token.id == token.head:
                error_sent_ids.append((sentence.id, len(sentence)))
                continue
            if token.deprel == 'root' or token.head == '0':
                # print(token.deprel)
                count_roots += 1
        if count_roots != 1:
            if sentence.id not in error_sent_ids:
                error_sent_ids.append((sentence.id, len(sentence)))

for id in error_sent_ids:
    print(f'{id[0]}\tTokens: {id[1]}')

print(f'No. of non-valid sentencens:\t{len(error_sent_ids)}')
print(f'No. of non-valid tokens:\t{sum(i[1] for i in error_sent_ids)}')
