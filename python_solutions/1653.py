class Solution:
    def minimumDeletions(self, s: str) -> int:
        bSToTheLeft = [0] # the left of the split, [0] is the beginning
        for i in range(len(s)):
            if s[i] == "b":
                bSToTheLeft.append(bSToTheLeft[-1] + 1)
            else:
                bSToTheLeft.append(bSToTheLeft[-1])
        
        aSToTheRight = [0 for i in range(len(s) + 1)]
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "a":
                aSToTheRight[i] = aSToTheRight[i + 1] + 1
            else:
                aSToTheRight[i] = aSToTheRight[i + 1]
        
        ans = 99999999
        for i in range(len(s) + 1):
            ans = min(ans, bSToTheLeft[i] + aSToTheRight[i])
        
        return ans
            
s = Solution()
print(s.minimumDeletions("aababbab"))
