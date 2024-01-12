class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        first = True
        for d in derived:
            if d == 1:
                first = not first
            else:
                first = first
        
        return first