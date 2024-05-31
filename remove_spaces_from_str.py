from typing import List


def remove_spaces(s: List[str]):
    if len(s) == 0:
        return

    l, r = 0, 1
    while r < len(s):
        if s[l] == ' ':
            while r < len(s) and s[r] == ' ':
                r += 1
            if r < len(s) and s[r] != ' ':
                s[l] = s[r]
                s[r] = ' '
        l += 1
        r += 1


if __name__ == '__main__':
    s = list("how are you")
    print(s)
    remove_spaces(s)
    print(s)
    s = list("ho")
    print(s)
    remove_spaces(s)
    print(s)
    s = list("h")
    print(s)
    remove_spaces(s)
    print(s)
    s = list("h ")
    print(s)
    remove_spaces(s)
    print(s)