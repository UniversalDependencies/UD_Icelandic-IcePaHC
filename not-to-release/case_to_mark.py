import pyconll

dev = "is_icepahc-ud-dev.conllu"
test = "is_icepahc-ud-test.conllu"
train = "is_icepahc-ud-train.conllu"

corpus = pyconll.load_from_file(dev)

for sentence in corpus:
    for token in sentence:
        if (
            (token.lemma == "þegar" or token.lemma == "ef")
            and token.upos == "ADP"
            and token.deprel == "case"
        ):
            if sentence[token.head].deprel != "root":
                sentence[token.head].deprel = "advcl"
            token.deprel = "mark"
            token.upos = "SCONJ"

with open(dev, "w", encoding="utf-8") as f:
    corpus.write(f)
