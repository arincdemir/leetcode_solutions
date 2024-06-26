from typing import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {2: "abc", 3: "def", 4: "ghi",
                   5: "jkl", 6: "mno", 7: "pqrs", 
                   8: "tuv", 9: "wxyz"}
        
        ans = []

        def dfs(i, cur):
            if i >= len(digits):
                ans.append("".join(cur))
                return

            for c in mapping[int(digits[i])]:
                cur.append(c)
                dfs(i + 1, cur)
                cur.pop()
            
        if digits == "":
            return []
        dfs(0, [])
        return ans