class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        dp = [0] * 1024
        dp[0] = 1
        ans = 0
        bitmask = 0
        for c in word:
            bitmask = bitmask ^ (1 << (ord(c) - ord("a")))
            ans += dp[bitmask]
            for i in range(10):
                oneFlipped = bitmask ^ (1 << i)
                ans += dp[oneFlipped]
            dp[bitmask] += 1

        return ans
