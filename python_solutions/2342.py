class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sumOfDigits(num):
            summ = 0
            while num > 0:
                summ += num % 10
                num = num // 10
            return summ
        
        digitSums = {}
        for num in nums:
            d = sumOfDigits(num)
            if d not in digitSums:
                digitSums[d] = [num, -1]
            else:
                maxes = digitSums[d]
                if num >= maxes[0]:
                    maxes[1] = maxes[0]
                    maxes[0] = num
                elif num > maxes[1]:
                    maxes[1] = num
        
        ans = -1
        for maxes in digitSums.values():
            if maxes[1] != -1:
                ans = max(ans, maxes[0] + maxes[1])
        
        return ans