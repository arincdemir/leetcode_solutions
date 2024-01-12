class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        maxUntilHere = [-1] * len(nums)
        maxUntilHere[0] = nums[0]
        for i in range(1, len(nums)):
            maxUntilHere[i] = max(maxUntilHere[i - 1], nums[i])

        minAfterHere = [99999999] * len(nums)
        minAfterHere[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            minAfterHere[i] = min(minAfterHere[i + 1], nums[i])

        ans = 0
        for i in range(1, len(nums) - 1):
            if maxUntilHere[i - 1] < nums[i] and nums[i] < minAfterHere[i + 1]:
                ans += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                ans += 1

        return ans