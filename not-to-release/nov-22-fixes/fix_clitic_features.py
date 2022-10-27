import pyconll
import sys

from utils.features import Features, ICE_Features
from utils.rules import lex_class_map


# a function to write the output to a file
def write_to_conllu(conllu_file, conll):
    with open(conllu_file, "w", encoding="utf-8") as f:
        for sentence in conll:
            # print(sentence.conll())
            f.write(sentence.conll())
            f.write("\n\n")


# a function to make all values in a dictionary a set of strings, if dictionary has items
def make_sets(d):
    for k, v in d.items():
        # print(k,v)
        if v:
            d[k] = set((v,))
    return d


# a function to add info to a misc column in a conllu file token
def add_tag_to_misc(misc, tag):
    misc["IFD_tag"] = set((tag,))
    return filter_none_values(misc)


# a function to filter out None values in a dictionary
def filter_none_values(d):
    return {k: v for k, v in d.items() if v is not None}


def filter_joined_tokens(sentence):
    return [token for token in sentence if "-" not in token.id]


def get_text_from_tokens(sentence):
    sentence = filter_joined_tokens(sentence)
    return " ".join([token.form for token in sentence])


def update_token_features_and_misc(token, tag_dict):
    # get tag from tag_dict of sentence
    # also, make sure the tag matches UPOS, i.e. lexical class
    ifd_tag = assert_correct_word_class(token, tag_dict.get(token.form, "x")[0])
    # the ICE_Features module used when ABLTagger 2018 is not able to tag a token
    if ifd_tag == "x":
        feats = ICE_Features(token.xpos).get_features()
    else:
        feats = Features(ifd_tag).features
    # overwrite the original features
    token.feats = filter_none_values(make_sets(dict(feats)))
    # overwrite the original misc column
    token.misc = add_tag_to_misc(token.misc, ifd_tag)

# compare tag and UPOS of a token and retrun 'x' if they are not equal
def assert_correct_word_class(token, tag):
    if not token.upos in lex_class_map[tag[0]]:
        tag = "x"
    return tag


if __name__ == "__main__":

    file_path = sys.argv[1]
    
    # load the conllu file
    conll = pyconll.load_from_file(file_path)

    sent_num = len(conll)
    runner = 0
    # loop through the sentences
    for sentence in conll:
        runner += 1
        sent_text = get_text_from_tokens(sentence)
        for token in sentence:
            # guard clause to only handle tokens with joined clitics
            if "-" not in token.id:
                continue
            else:
                # token ids for joined tokens are in the form of 1-2, 1-3, etc.
                token_id_1, token_id_2 = token.id.split("-")
                # the Features module used to tag the sentence as a whole
                # (Note: ABLTagger 2018 is used to tag the sentences)
                tag_dict = Features.tagged_sent(sent_text)
                update_token_features_and_misc(sentence[token_id_1], tag_dict)
                update_token_features_and_misc(sentence[token_id_2], tag_dict)

        #     print(token.id, token.form, token.lemma, token.upos, token.xpos, token.feats, token.head, token.deprel, token.deps, token.misc)
        # input()

        # print the progress
        if runner % 10 == 0:
            print(f"Processed sentence {runner} of {sent_num}", end="\r")
       

    # write the new conllu file
    write_to_conllu(file_path, conll)
