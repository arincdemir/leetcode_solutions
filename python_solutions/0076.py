class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars = {}
        for c in t:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
        
        num = len(chars)

        left = 0
        right = 0
        minn = s + "s"
        while right <= len(s):
            if num > 0:
                if right == len(s):
                    break
                if s[right] in chars:
                    if chars[s[right]] == 1:
                        num -= 1
                    chars[s[right]] -= 1
                right += 1
            else:
                if right - left < len(minn):
                    minn = s[left:right]
                if s[left] in chars:
                    if chars[s[left]] == 0:
                        num += 1
                    chars[s[left]] += 1
                left += 1

        if len(minn) > len(s):
            return ""
        else:
            return minn

s = Solution()
print(s.minWindow("ADOBECODEBANC","ABC"))