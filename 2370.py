class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        prevTable = [-1] * (ord("z") - ord("a") + 1)

        for i in range(len(s)):
            newTable = [-1] * (ord("z") - ord("a") + 1)
            newTable[ord(s[i]) - ord("a")] = 1
            for j in range(len(prevTable)):
                newTable[j] = max(prevTable[j], newTable[j])
                if abs(ord(s[i]) - ord("a") - j) <= k:
                    newTable[ord(s[i]) - ord("a")] = max(newTable[ord(s[i]) - ord("a")], prevTable[j] + 1)

            prevTable = newTable

        return max(prevTable)
