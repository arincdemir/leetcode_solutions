from typing import *
class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort(key= lambda x: x[0])
        ans = 0
        left = 0
        right = 0
        window = 0
        while left < len(tiles) and right < len(tiles):
            if tiles[left][0] + carpetLen > tiles[right][1]:
                window += tiles[right][1] - tiles[right][0] + 1
                ans = max(ans, window)
                right += 1
            else:
                partial = max(0, tiles[left][0] + carpetLen - tiles[right][0])
                ans = max(ans, window + partial)
                window -= tiles[left][1] - tiles[left][0] + 1
                left += 1
            
        
        return ans
            
            
