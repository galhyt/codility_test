class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        while len(s) > 0:
            b = s[0]
            s = s[1:]
            if b in '({[':
                stack.append(b)
            else:
                if not stack:
                    return False
                o = stack.pop(-1)
                if (b == '}' and o != '{') or (b == ')' and o  != '(') or (b == ']' and o != '['):
                    return False
        return not stack


if __name__ == '__main__':
    s = "()"
    sol = Solution()
    print(sol.isValid(s))
