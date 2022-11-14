import re
import sys

POSS_LEMMAS = {
    "minn",
    "sinn",
    "vor",
    "þinn",
}

IFD = r"IFD_tag=fe"
OLD = r"\|PronType=Prs"
NEW = r"|Poss=Yes|PronType=Prs"

# function that reads a file and returns an iterator of the lines
def read_file(file_name):
    with open(file_name, "r") as f:
        for line in f:
            yield line


# iterate over a list and write to file
def write_file(file_name, lines):
    with open(file_name, "w") as f:
        for line in lines:
            f.write(line)

def modify_line(line):
    lemma = line.split("")[2]
    if re.search(IFD, line) and lemma in POSS_LEMMAS:
        line = re.sub(OLD, NEW, line)
    return line

def main():

    # command line argument saved as input file path
    fh = sys.argv[1] if sys.argv[1] else sys.stdout
    # read file
    lines = read_file(fh)
    modified_lines = [modify_line(line) for line in lines]
    write_file(fh, modified_lines)


if __name__ == "__main__":
    main()
