class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1List = [c for c in s1]
        s2List = [c for c in s2]
        s1List.sort()
        s2List.sort()

        s1CanBreak = True
        for i in range(len(s1List)):
            if s1List[i] >= s2List[i]:
                continue
            else:
                s1CanBreak = False
                break
        
        if s1CanBreak:
            return True
        
        s2CanBreak = True
        for i in range(len(s2List)):
            if s2List[i] >= s1List[i]:
                continue
            else:
                s2CanBreak = False
                break
        
        return s2CanBreak