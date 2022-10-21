# Script for getting UD sentence IDs that are affected by the (CODE {COM:threedots})) error.
# The script reads all trees from the IcePaHC corpus, searches for the substring (CODE {COM:threedots})) and 
# gets the sentence ID from the tree. These are compared to the UD corpus and the UD sentence IDs that contain 
# the X_IDs from the threedots list are returned.
# Note: The paths are relative to another location, so you will have to change them and the original (up to date) 
# IcePaHC .psd files will need to be downloaded seperately (see https://github.com/antonkarl/icecorpus). 
# The script also uses pyconll to read the UD corpus and get the UD sentence IDs that contain the X_IDs 
# from the IcePaHC corpus.

import os
import re
import pyconll


def get_files_in_subdir(subdirectory):
    files = os.listdir(subdirectory)
    return files


def get_conllu_files_in_subdir(subdirectory):
    files = os.listdir(subdirectory)
    conllu_files = []
    for file in files:
        if file.endswith(".conllu"):
            conllu_files.append(file)
    return conllu_files


def write_ud_ids_to_file(ud_ids, filename):
    with open(filename, "w") as f:
        for ud_id in ud_ids:
            f.write(ud_id + "\n")


def split_file_into_trees(file):
    trees = file.split("\n\n")
    return trees


# function that reads all files in a subdieroctry, splits them into trees and returns a list of trees
def get_icepahc_trees(subdirectory):
    files = get_files_in_subdir(subdirectory)
    all_trees = []
    for file in files:
        if file == "additions2019":
            continue
        with open(subdirectory + "/" + file, "r") as f:
            file = f.read()
            trees = split_file_into_trees(file)
            all_trees += trees
    return all_trees


# function that searches a tree for a substring
def search_for_substring_in_tree(string, substring):
    if substring in string:
        return True
    else:
        return False


# funtion that gets the sentence ID from a tree with regex
def get_sentence_id_from_tree(tree):
    sentence_id = re.search(r"\(ID.*\)\)", tree)
    return sentence_id


# get all sentence ids that contain substring
def get_sentence_ids_containing_substring(substring, trees, clean):
    sentence_ids = []
    for tree in trees:
        if search_for_substring_in_tree(tree, substring):
            sentence_id = (
                get_sentence_id_from_tree(tree)[0]
                if get_sentence_id_from_tree(tree)
                else "missing"
            )
            if clean:
                sentence_id = sentence_id.replace("(ID ", "").replace("))", "")
            sentence_ids.append(sentence_id)
    return sentence_ids


# write sentence ids to file
def write_sentence_ids_to_file(sentence_ids, filename):
    with open(filename, "w") as f:
        for sentence_id in sentence_ids:
            f.write(sentence_id + "\n")


def get_ud_corpus_from_file(filename):
    print(f"Loading file: {filename}")
    ud_corpus = pyconll.load_from_file(filename)
    return ud_corpus


# get the x_ids from the sentence object, or x_id if there is only one
def get_icepahc_ids_from_sentence(sentence):
    try:
        x_ids = sentence.meta_value("X_ID")
    except KeyError:
        x_ids = sentence.meta_value("X_IDs")
    return x_ids


# pyconll used to read a UD corpus and get the UD IDs ids that contain the XIDs from the threedots list
def get_ud_ids_from_xids(threedot_ids):
    affected_ud_ids = []
    ud_files = get_conllu_files_in_subdir("../UD_Icelandic-IcePaHC/")
    for file in ud_files:
        ud_ids = []
        ud_corpus = get_ud_corpus_from_file("../UD_Icelandic-IcePaHC/" + file)
        print(f"Number of sentences in file: {len(ud_corpus)}")
        for sentence in ud_corpus:
            ud_id = sentence.id
            x_id = get_icepahc_ids_from_sentence(sentence)
            for id in threedot_ids:
                if id in x_id:
                    ud_ids.append(ud_id)
        affected_ud_ids.append(ud_ids)
        print(f"Number of affected UD IDs in file: {len(ud_ids)}")
    print(f"Total number of affected UD IDs: {len([j for i in affected_ud_ids for j in i])}")
    return affected_ud_ids


if __name__ == "__main__":
    THREEDOTS = "(CODE {COM:threedots}))"
    # get all trees
    trees = get_icepahc_trees("../icecorpus/finished/")
    # get all sentence ids that contain the substring "þrjú"
    threedot_ids = get_sentence_ids_containing_substring(THREEDOTS, trees, clean=True)
    # write sentence ids to file
    write_sentence_ids_to_file(threedot_ids, "threedots_ids.txt")
    # gather ids of all affected sentences
    affected_sentence_ids = get_ud_ids_from_xids(threedot_ids)
    write_ud_ids_to_file(affected_sentence_ids[0], "threedots_ud_ids_train.txt")
    write_ud_ids_to_file(affected_sentence_ids[1], "threedots_ud_ids_test.txt")
    write_ud_ids_to_file(affected_sentence_ids[2], "threedots_ud_ids_dev.txt")
    # combine sublists into one list
    combined_ids = [j for i in affected_sentence_ids for j in i]
    write_ud_ids_to_file(combined_ids, "threedots_ud_ids_all.txt")
