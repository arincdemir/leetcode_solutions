class Solution:
    def smallestSubsequence(self, s: str) -> str:
        lastPos = {}
        for i, c in enumerate(s):
            lastPos[c] = i

        stack = []
        for i, c in enumerate(s):
            if c in stack:
                continue
            while stack and stack[-1] > c and lastPos[stack[-1]] > i:
                stack.pop()
            stack.append(c)

        return "".join(stack)