from typing import *
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        numberOfTasks = {}
        
        for task in tasks:
            numberOfTasks[task] = numberOfTasks.get(task, 0) + 1
        
        ready = [(-count , task) for task, count in numberOfTasks.items()]
        heapq.heapify(ready)

        cooldown = []
        time = 0
        while numberOfTasks:
            if cooldown and cooldown[0][0] == time:
                _, task = heapq.heappop(cooldown)
                heapq.heappush(ready, (-numberOfTasks[task], task))

            if ready:
                count, task = heapq.heappop(ready)
                count = -count
                time += 1
                if count == 1:
                    numberOfTasks.pop(task)
                else:
                    numberOfTasks[task] -= 1
                    heapq.heappush(cooldown, (time + n, task))

            else:
                time, task = heapq.heappop(cooldown)
                time += 1
                if numberOfTasks[task] == 1:
                    numberOfTasks.pop(task)
                else:
                    numberOfTasks[task] -= 1
                    heapq.heappush(cooldown, (time + n, task))
        
        return time
                

s = Solution()
print(s.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))