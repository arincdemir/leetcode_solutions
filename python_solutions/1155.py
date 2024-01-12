class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = {}
        mod = 1000000007

        def dfs(i, sumNeeded):
            if (i, sumNeeded) in dp:
                return dp[(i, sumNeeded)]
            if (i == n and sumNeeded == 0):
                return 1
            elif (i == n):
                return 0
            if sumNeeded < 0:
                return 0
            
            ways = 0
            for j in range(1, k + 1):
                ways += dfs(i + 1, sumNeeded - j)
            
            dp[(i, sumNeeded)] = ways
            return ways
        
        return dfs(0, target) % mod

s = Solution()
print(s.numRollsToTarget(30, 30, 500))