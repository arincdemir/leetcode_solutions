from typing import *

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for a in asteroids:
            if a > mass:
                return False
            else:
                mass += a

        return True