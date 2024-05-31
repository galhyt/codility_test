from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        sorted_strs = sorted([(s, ''.join(sorted(list(s)))) for s in strs], key=lambda t: t[1])

        output = []
        j = 0
        for i in range(len(strs)-1):
            if j == len(output):
                output.append([sorted_strs[i][0]])
            if sorted_strs[i][1] == sorted_strs[i+1][1]:
                output[j].append(sorted_strs[i+1][0])
            else:
                if i == len(strs)-2:
                    output.append([sorted_strs[i+1][0]])
                j += 1
        return output


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # strs = ["","b"]
    strs = ['abc', 'abcd', 'def', 'cba']
    sol = Solution()
    print(sol.groupAnagrams(strs))
