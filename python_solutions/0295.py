import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        self.even = True
        self.median = []

    def addNum(self, num: int) -> None:
        if not self.median:
            self.median.append(num)
            self.even = False
            return

        if self.even:
            self.even = False
            if num <= self.median[0]:
                heapq.heappush(self.left, -num)
                heapq.heappush(self.right, self.median[1])
                self.median.pop()
            elif num >= self.median[1]:
                heapq.heappush(self.right, num)
                heapq.heappush(self.left, -self.median[0])
                self.median.pop(0)
            else:
                heapq.heappush(self.left, -self.median[0])
                heapq.heappush(self.right, self.median[1])
                self.median = [num]
        else:
            self.even = True
            if num <= self.median[0]:
                heapq.heappush(self.left, -num)
                self.median.insert(0, -heapq.heappop(self.left))
            else:
                heapq.heappush(self.right, num)
                self.median.append(heapq.heappop(self.right))

    def findMedian(self) -> float:
        return sum(self.median) / len(self.median)


