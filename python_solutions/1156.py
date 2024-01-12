def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        charLastAndFirst = {}
        for i in range(len(text)):
            c = text[i]
            if c in charLastAndFirst:
                charLastAndFirst[c][1] = i
            else:
                charLastAndFirst[c] = [i, i]
        
        arr = [c for c in text]
        ans = 0
        ssStart = 0
        prev = arr[0]
        for i in range(1, len(arr)):
            if arr[i] == prev:
                continue
            else:
                end = i - 1
                swappedIndex = 0
                lastAndFirst = charLastAndFirst[prev]
                if lastAndFirst[0] < ssStart:
                    swappedIndex = lastAndFirst[0]
                elif lastAndFirst[1] != i - 1:
                    swappedIndex = lastAndFirst[1]
                elif lastAndFirst[0] != lastAndFirst[1]:
                    swappedIndex = lastAndFirst[0]
                    ssStart += 1
                else:
                    swappedIndex = i
                swap(arr, i, swappedIndex)
                while end + 1 < len(arr) and arr[end + 1] == prev:
                    end += 1
                swap(arr, i, swappedIndex)
                ans = max(ans, end - ssStart + 1)
                prev = arr[i]
                ssStart = i
        
        if charLastAndFirst[prev][0] != ssStart:
            ssStart -= 1
        ans = max(ans, len(arr)  - ssStart)
        return ans

s = Solution
print(s.maxRepOpt1(s, "babbaaabbbbbaa"))
