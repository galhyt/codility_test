

class Solution:
    def isMatch(self, s: str, p: str, char_with_asteric: str = None) -> bool:
        """
        abcddefg
        abcd.*g
        abcd*
        """
        i = 0
        j = 0
        if char_with_asteric:
            while i < len(s) and (s[i] == char_with_asteric or char_with_asteric == '.'):
                i += 1
            repeated_num = i
            for k in range(repeated_num+1):
                if self.isMatch(s[k:], p):
                    return True
            return False
        else:
            while j < len(p):
                if j+1 >= len(p) or p[j+1] != '*':
                    if i == len(s):  # no more characters left in s
                        return False
                    if s[i] == p[j] or p[j] == '.':
                        i += 1
                        j += 1
                    else:
                        return False
                else:
                    return self.isMatch(s[i:], p[j+2:], p[j])

            return i == len(s)  # all characters in s are matched


if __name__ == '__main__':
    sol = Solution()
    s = "abc"
    p = ".*c"
    s = "aab"
    p = "c*a*b"
    print(sol.isMatch(s, p))
