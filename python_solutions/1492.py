import math

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        factorsReverse = []
        sqrt = math.sqrt(n)
        for i in range(1, math.ceil(sqrt + 0.00001)):
            if n % i == 0:
                factors.append(i)
                if i != sqrt:
                    factorsReverse.append(n // i)

        factorsReverse.reverse()
        factors.extend(factorsReverse)

        if k > len(factors):
            return -1
        else:
            return factors[k - 1]
