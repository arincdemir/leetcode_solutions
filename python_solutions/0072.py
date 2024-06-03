class Solution:
    def minDistance(self, word1: str, word2: str, dp={}) -> int:
        if len(word1) == 0:
            return len(word2)
        
        if len(word2) == 0:
            return len(word1)
        
        if (word1, word2) in dp:
            return dp[(word1, word2)]
        
        # if first char is equal
        ans = float("inf")
        if word1[0] == word2[0]:
            ans = min(ans, self.minDistance(word1[1:], word2[1:]))
        
        # replace first char
        ans = min(ans, self.minDistance(word1[1:], word2[1:]) + 1)
        # remove first char
        ans = min(ans, self.minDistance(word1[1:], word2) + 1)
        # insert first char
        ans = min(ans, self.minDistance(word1, word2[1:]) + 1)

        dp[(word1, word2)] = ans
        return ans