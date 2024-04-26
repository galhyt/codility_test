from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        char_num = 0
        i = 0
        while i < len(words):
            char_num += len(words[i])
            if char_num + i < maxWidth:
                i += 1
            else:
                if char_num + i > maxWidth:
                    char_num -= len(words[i])
                    i -= 1
                line = [words.pop(0) for _ in range(i+1)]
                output.append(self.get_line(line, char_num, maxWidth, len(words) == 0))
                i = 0
                char_num = 0

        if len(words) > 0:
            line = words
            output.append(self.get_line(line, char_num, maxWidth, True))

        return output

    def get_line(self, line: List[str], char_num: int, maxWidth: int, last_line: bool):
        n = len(line)
        char_num += n - 1
        add_spaces = maxWidth - char_num
        if not last_line:
            if n > 1:
                word_space = int(add_spaces / (n-1))
                left_most_spaces = add_spaces % (n-1)
                text = ''.join(line[i] + ' ' + ' ' * (word_space + 1) for i in range(left_most_spaces)) + \
                       ''.join(line[i] + ' ' + ' ' * word_space for i in range(left_most_spaces, n - 1)) + \
                       line[n - 1]
            else:
                text = line[0]
                add_spaces = maxWidth - len(text)
                text += ' ' * add_spaces
        else:
            text = ' '.join(line)
            add_spaces = maxWidth - len(text)
            text += ' ' * add_spaces
        return text


if __name__ == '__main__':
    sol = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print(sol.fullJustify(words, maxWidth))

    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    maxWidth = 16
    print(sol.fullJustify(words, maxWidth))

    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
             "Art", "is", "everything", "else", "we", "do"]
    maxWidth = 20
    print(sol.fullJustify(words, maxWidth))
