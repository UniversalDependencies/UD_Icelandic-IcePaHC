

import pyconll
import pyconll.util
import sys
import os
import argparse

conllu_path = sys.argv[1]

log_file = open('clitic_info.txt', 'w+')

for conllu_file in os.listdir(conllu_path):
    print(conllu_file)
    file = pyconll.load_from_file(os.path.join(conllu_path, conllu_file))
    for sentence in file:
        for token in sentence:
            if '-' in token.id:
                log_file.write(token.form  \
                    + '\t' + sentence[token.id.split('-')[0]].form \
                    + '\t' + sentence[token.id.split('-')[1]].form )
                log_file.write('\n')

log_file.close()
