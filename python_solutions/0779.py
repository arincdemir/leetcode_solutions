class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        base = self.kthGrammar(n - 1, (k + 1) // 2)
        if (base == 0 and k % 2 == 0) or (base == 1 and k % 2 == 1):
            return 1
        else:
            return 0