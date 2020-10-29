
import pyconll
import os
import re
import sys

def get_error_sents(path):
    error_sent_ids = []
    for file in os.listdir(path):
        conll = pyconll.iter_from_file(os.path.join(path, file))
        for sentence in conll:
            count_roots = 0
            for token in sentence:
                if token.id == token.head:
                    error_sent_ids.append(sentence.id)
                    continue
                if token.deprel == 'root' or token.head == '0':
                    # print(token.deprel)
                    count_roots += 1
            if count_roots != 1:
                if sentence.id not in error_sent_ids:
                    error_sent_ids.append(sentence.id)
    return error_sent_ids

def fix_sent_ids(conll, file_count, total_count):
    lines = conll.split('\n')
    s_id = lines[1]
    x_id = lines[0]
    new_s_id = s_id.split(',')[0]+f',{file_count}.{total_count}'
    new_lines = [new_s_id, x_id] + lines[2:]
    return '\n'.join(new_lines)

SPLITS = {
    'train': ['1150.homiliubok.rel-ser',
              '1210.thorlakur.rel-sag',
              '1250.sturlunga.nar-sag',
              '1260.jomsvikingar.nar-sag',
              '1270.gragas.law-law',
              '1275.morkin.nar-his',
              '1300.alexander.nar-sag',
              '1310.grettir.nar-sag',
              '1325.arni.nar-sag',
              '1350.finnbogi.nar-sag',
              '1400.gunnar.nar-sag',
              '1400.viglundur.nar-sag',
              '1450.ectorssaga.nar-sag',
              '1450.judit.rel-bib',
              '1450.vilhjalmur.nar-sag',
              '1480.jarlmann.nar-sag',
              '1525.erasmus.nar-sag',
              '1540.ntjohn.rel-bib',
              '1593.eintal.rel-oth',
              '1611.okur.rel-oth',
              '1650.illugi.nar-sag',
              '1659.pislarsaga.bio-aut',
              '1661.indiafari.bio-tra',
              '1675.armann.nar-fic',
              '1675.magnus.bio-oth',
              '1675.modars.nar-fic',
              '1680.skalholt.nar-rel',
              '1725.biskupasogur.nar-rel',
              '1790.fimmbraedra.nar-sag',
              '1791.jonsteingrims.bio-aut',
              '1830.hellismenn.nar-sag',
              '1835.jonasedli.sci-nat',
              '1859.hugvekjur.rel-ser',
              '1861.orrusta.nar-fic',
              '1882.torfhildur.nar-fic',
              '1888.vordraumur.nar-fic',
              '1907.leysing.nar-fic',
              '1908.ofurefli.nar-fic',
              '1985.margsaga.nar-fic',
              '1985.sagan.nar-fic',
              '2008.mamma.nar-fic',],

    'test': ['1150.firstgrammar.sci-lin',
              '1210.jartein.rel-sag',
              '1350.marta.rel-sag',
              '1450.bandamenn.nar-sag',
              '1400.gunnar2.nar-sag',
              '1540.ntacts.rel-bib',
              '1628.olafuregils.bio-tra',
              '1745.klim.nar-fic',
              '1850.piltur.nar-fic',
              '1920.arin.rel-ser',],

    'dev': ['1250.thetubrot.nar-sag',
            '1350.bandamennM.nar-sag',
            '1475.aevintyri.nar-rel',
            '1525.georgius.nar-rel',
            '1630.gerhard.rel-oth',
            '1720.vidalin.rel-ser',
            '1888.grimur.nar-fic',
            '1883.voggur.nar-fic',
            '1902.fossar.nar-fic',
            '2008.ofsi.nar-sag',]}

PREFIXES = ['dev', 'test', 'train']

# TEST_PATH = '../../CoNLLU'
TEST_PATH = sys.argv[1]
ERROR_SENTS = get_error_sents(TEST_PATH)

print(f'\nNo. of non-valid sentencens:\t{len(ERROR_SENTS)}\n')

for prefix in PREFIXES:
    total_sentences = 0
    output_file = f'is_icepahc-ud-{prefix}.conllu'
    print(f'Writing to file: {output_file}')
    with open(output_file, 'a+') as f, open('error_sents.conllu', 'a+') as err_f:
        for file in SPLITS[prefix]:
            
            file_sentences = 0
            
            file += '.conllu'
            print(f'\t{file}')
            conll = pyconll.iter_from_file(os.path.join(TEST_PATH, file))
            for sentence in conll:
                file_sentences +=1
                total_sentences +=1
                # if sentence.id in ERROR_SENTS:
                #     err_f.write(sentence.conll())
                #     err_f.write('\n\n')
                # else:
                output_conll = fix_sent_ids(sentence.conll(), file_sentences, total_sentences)
                f.write(output_conll)
                f.write('\n\n')

                
