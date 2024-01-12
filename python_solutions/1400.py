class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        if k > len(s):
            return False

        frequencies = dict()
        for c in s:
            frequencies[c] = frequencies.get(c, 0) + 1

        for c, f in frequencies.items():
            if f % 2 == 1:
                k -= 1

        if k >= 0:
            return True
        else:
            return False
