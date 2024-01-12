from typing import *
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = dict()

        def dfs(bought: bool, i: int):
            if i == len(prices) - 1:
                if bought:
                    return prices[i] - fee
                else:
                    return 0

            if (bought, i) in dp:
                return dp[(bought, i)]

            profit = 0
            if bought:
                sell = dfs(False, i + 1) + prices[i] - fee
                skip = dfs(bought, i + 1)
                profit = max(sell, skip)
            else:
                buy = dfs(True, i + 1) - prices[i]
                skip = dfs(bought, i + 1)
                profit = max(buy, skip)

            dp[(bought, i)] = profit
            return profit

        return dfs(False, 0)


