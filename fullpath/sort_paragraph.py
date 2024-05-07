import re
from functools import reduce

letters_order = {l: i for i, l in enumerate("ABGDHVZJTYKLMNSIPXQRWUCEFO")}
a_ord = ord('A')


def sort_paragraph(paragraph: str):
    # extract words only from the paragraph
    arr = re.split(r'[^\w]+', paragraph)

    # sorted function can sort words alphabetically, so the key for each word is its alphabetical reflection according
    # to letters_order. e.g. "Lorem"'s key is "LZTXM"
    arr = sorted(arr, key=lambda word: reduce(lambda w, l: w + chr(a_ord + letters_order[l.upper()]), word, ''))

    return " ".join(arr)


if __name__ == '__main__':
    par = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
    print(sort_paragraph(par))
