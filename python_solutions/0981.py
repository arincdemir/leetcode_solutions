from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        llist = self.dict[key]
        l = 0
        r = len(llist) - 1
        while l <= r:
            mid = (l + r) // 2
            if llist[mid][0] == timestamp:
                return llist[mid][1]
            elif llist[mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        
        if l == 0:
            return ""
        else:
            return llist[l - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)