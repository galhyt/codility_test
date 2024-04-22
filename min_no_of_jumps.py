

#User function Template for python3
class Solution:
    def _min_jumps(self, arr, s, n):
        jumps = arr[s]
        if jumps >= n-1: return 1
        return 1 + min((self._min_jumps(arr, j, n-j) for j in range(jumps, 0, -1)))

    def minJumps(self, arr, n):
        return self._min_jumps(arr, 0, n)


#{
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr,n)
        print(ans)
# } Driver Code Ends