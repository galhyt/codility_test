# User function Template for python3

# Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self, arr, n, s):
        if s == 0:
            try:
                start = arr.index(0)
                return start + 1, start + 1
            except ValueError:
                return -1,
        start = 0
        rem_s = s
        end = start
        while end < n:
            rem_s -= arr[end]
            if rem_s < 0:
                while rem_s < 0:
                    rem_s += arr[start]
                    start += 1
            if rem_s == 0:
                return start + 1, end + 1

            end += 1

        return -1,

# Write your code here

# {
# Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        NS = input().strip().split()
        N = int(NS[0])
        S = int(NS[1])

        A = list(map(int, input().split()))
        ob = Solution()
        ans = ob.subArraySum(A, N, S)

        for i in ans:
            print(i, end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends