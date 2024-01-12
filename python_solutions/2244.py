from typing import *

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        frequencies = dict()
        for task in tasks:
            frequencies[task] = frequencies.get(task, 0) + 1

        ans = 0
        for difficulty, frequency in frequencies.items():
            if frequency == 1:
                return -1

            if frequency % 3 == 0:
                ans += frequency // 3
            elif frequency % 3 == 1:
                ans += frequency // 3 + 1
            elif frequency % 3 == 2:
                ans += frequency // 3 + 1

        return ans