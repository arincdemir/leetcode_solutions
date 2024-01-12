class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stack = [start]
        visited = set()
        while stack:
            elem = stack.pop()
            if arr[elem] == 0:
                return True
            if elem in visited:
                continue
            visited.add(elem)
            if elem + arr[elem] < len(arr):
                stack.append(elem + arr[elem])
            if elem - arr[elem] >= 0:
                stack.append(elem - arr[elem])
        
        return False

