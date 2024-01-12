class Solution:
    def frequencySort(self, s: str) -> str:
        frequencies = dict()
        for c in s:
            frequencies[c] = frequencies.get(c, 0) + 1

        frequencies = list(frequencies.items())
        frequencies.sort(key=lambda x: x[1], reverse=True)

        ans = []
        for c, f in frequencies:
            for i in range(f):
                ans.append(c)

        return "".join(ans)