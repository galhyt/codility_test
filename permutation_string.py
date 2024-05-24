class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        for c in s1:
            s1_dict.setdefault(c, 0)
            s1_dict[c] += 1

        perm_dict = {}
        l, r = 0, 0
        n = len(s2)

        while r < n:
            r_in_s1 = s1_dict.get(s2[r], 0)
            if r_in_s1:
                r_in_perm = perm_dict.get(s2[r], 0) + 1
                perm_dict[s2[r]] = r_in_perm
                if r_in_perm > r_in_s1:
                    while perm_dict[s2[r]] > r_in_s1:
                        perm_dict[s2[l]] -= 1
                        l += 1
                else:
                    if r - l + 1 == len(s1):
                        return True
                r += 1
            else:
                perm_dict = {}
                l = r + 1
                r = l

        return False


if __name__ == '__main__':
    s1 = "ky"
    s2 = "ainwkckifykxlribaypk"
    sol = Solution()
    print(sol.checkInclusion(s1, s2))
