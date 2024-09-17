import udapi

dev = "is_icepahc-ud-dev.conllu"

doc = udapi.Document(dev)
for node in doc.nodes:
    if node.lemma in {"þegar", "ef", "nema", "þótt", "þó"} and node.upos == "ADP" and node.deprel == "case":
        if node.parent.deprel != "root":
            node.parent.deprel = "advcl"
        node.deprel = "mark"
        node.upos = "SCONJ"
doc.store_conllu(dev)
