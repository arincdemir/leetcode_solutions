from typing import *

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        chars = {}
        vote = votes[0]
        for c in vote:
            chars[c] = [0] * len(vote)

        for vote in votes:
            for i in range(len(vote)):
                chars[vote[i]][i] += 1

        def lessThan(x, y):
            vx = chars[x]
            vy = chars[y]
            index = 0
            while index < len(vx) and vx[index] == vy[index]:
                index += 1
            if index == len(vx):
                return x > y
            else:
                return vx[index] < vy[index]

        ans = []
        for c in chars.keys():
            ans.append(c)
            index = len(ans) - 1
            while index > 0 and lessThan(c, ans[index - 1]):
                ans[index] = ans[index - 1]
                ans[index - 1] = c
                index -= 1

        ans.reverse()
        return "".join(ans)
