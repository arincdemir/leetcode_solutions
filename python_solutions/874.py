class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstaclesSet = set()
        for o in obstacles:
            obstaclesSet.add((o[0], o[1]))
        
        def turnRight(direction):
            if direction == (0, 1):
                return (1, 0)
            elif direction == (1, 0):
                return (0, -1)
            elif direction == (0, -1):
                return (-1, 0)
            else:
                return (0, 1)
        
        def turnLeft(direction):
            right = turnRight(direction)
            return (-right[0], -right[1])
        
        def calcDistance(coords):
            return coords[0] ** 2 + coords[1] ** 2
        
        coords = [0, 0]
        ans = 0
        direction = (0, 1)
        for com in commands:
            if com == -2:
                direction = turnLeft(direction)
            elif com == -1:
                direction = turnRight(direction)
            else:
                next = (coords[0] + direction[0], coords[1] + direction[1])
                while com > 0 and next not in obstaclesSet:
                    com -= 1
                    coords[0] += direction[0]
                    coords[1] += direction[1]
                    ans = max(ans, calcDistance(coords))
                    next = (coords[0] + direction[0], coords[1] + direction[1])
        
        return ans