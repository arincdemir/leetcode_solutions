class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 1
        curOddBegin = 0
        curEvenBegin = 0
        for i in range(len(arr) - 1):
            if i % 2 == 0:
                if arr[i] < arr[i + 1]:
                    curEvenBegin = i + 1
                    ans = max(ans, i + 1 - curOddBegin + 1)
                elif arr[i] > arr[i + 1]:
                    curOddBegin = i + 1
                    ans = max(ans, i + 1 - curEvenBegin + 1)
                else:
                    curEvenBegin = i + 1
                    curOddBegin = i + 1
            else:
                if arr[i] < arr[i + 1]:
                    curOddBegin = i + 1
                    ans = max(ans, i + 1 - curEvenBegin + 1)

                elif arr[i] > arr[i + 1]:
                    curEvenBegin = i + 1
                    ans = max(ans, i + 1 - curOddBegin + 1)
                else: 
                    curOddBegin = i + 1
                    curEvenBegin = i + 1
    
        
        return ans