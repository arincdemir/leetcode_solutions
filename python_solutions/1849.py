class Solution:
    def splitString(self, s: str) -> bool:
        def canFormValidSplit(string, value):
            for i in range(1, len(string) + 1):
                if(int(string[0:i]) == value):
                    if i == len(string):
                        return True
                    elif canFormValidSplit(string[i::], value - 1):
                        return True
                    if value != 0:
                        break
            return False
        
        for i in range(1, len(s) + 1):
            value = int(s[0:i])
            if canFormValidSplit(s[i::], value - 1):
                return True
        return False

        
                
s = Solution()
print(s.splitString("200100"))