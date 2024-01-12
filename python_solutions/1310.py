class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        preXOR = [arr[0]]
        for i in range(1, len(arr)):
            preXOR.append(preXOR[i - 1] ^ arr[i])

        ans = []
        
        for l, r in queries:
            ans.append(preXOR[r] ^ preXOR[l] ^ arr[l])
        
        return ans