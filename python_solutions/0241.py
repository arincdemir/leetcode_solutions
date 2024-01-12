from typing import *

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        tokens = []
        lastIndex = 0
        for i in range(len(expression)):
            if expression[i] in ["+", "-", "*"]:
                tokens.append(int(expression[lastIndex : i]))
                tokens.append(expression[i])
                lastIndex = i + 1

        tokens.append(int(expression[lastIndex::]))

        def ways(tokens):
            if len(tokens) == 1:
                return tokens

            ans = list()
            for i in range(1, len(tokens), 2):
                operator = tokens[i]
                left = ways(tokens[0:i])
                right = ways(tokens[i + 1::])
                for l in left:
                    for r in right:
                        if operator == "+":
                            ans.append(l + r)
                        elif operator == "-":
                            ans.append(l - r)
                        else:
                            ans.append(l * r)

            return ans

        return ways(tokens)
