from typing import *

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10 ** 9 + 7
        powers = []
        degree = 0
        while n > 0:
            if n % 2 == 0:
                pass
            else:
                powers.append(degree)
            degree += 1
            n = n // 2

        preProduct = [powers[0]]
        for i in range(1, len(powers)):
            preProduct.append(preProduct[i - 1] + powers[i])

        ans = []
        for left, right in queries:
            product = 2 ** (preProduct[right] - preProduct[left] + powers[left])
            ans.append(product % mod)

        return ans