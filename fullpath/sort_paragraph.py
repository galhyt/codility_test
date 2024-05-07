import re
from functools import reduce

letters_order = {l: i for i, l in enumerate("ABGDHVZJTYKLMNSIPXQRWUCEFO")}
a_ord = ord('A')


def sort_paragraph(paragraph: str):
    # extract words only from the paragraph
    arr = re.split(r'[^\w]+', paragraph)

    word_dict = {w: 0 for w in arr}
    def _key(word: str):
        word_dict[word] += 1
        return reduce(lambda w, l: w + chr(a_ord + letters_order[l.upper()]), word, '')

    # sorted function can sort words alphabetically, so the key for each word is its alphabetical reflection according
    # to letters_order. e.g. "Lorem"'s key is "LZTXM"
    arr = sorted(arr, key=_key)

    return " ".join(arr), word_dict


if __name__ == '__main__':
    par = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
    print(sort_paragraph(par))
