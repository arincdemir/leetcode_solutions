class Node:
    def __init__(self,key = 0, val = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.hashMap = {}

    def get(self, key: int) -> int:
        if key in self.hashMap:
            elem = self.hashMap[key]
            self.put(key, elem.val)
            return elem.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.hashMap and len(self.hashMap) > self.capacity - 1:
            self.hashMap.pop(self.head.key)
            self.head = self.head.next
            if len(self.hashMap) == 0:
                self.tail = None
            else:
                self.head.prev = None

        if key in self.hashMap:
            old = self.hashMap[key]
            self.hashMap.pop(key)
            if self.head == old and self.tail == old:
                self.head = None
                self.tail = None
            elif self.head == old:
                self.head = self.head.next
                self.head.prev = None
                old.next = None
            elif self.tail == old:
                self.tail = self.tail.prev
                self.tail.next = None
                old.prev = None
            else:
                prev = old.prev
                next = old.next
                old.prev = None
                old.next = None
                prev.next = next
                next.prev = prev
        
        if len(self.hashMap) == 0:
            newNode = Node(key, value)
            self.head = newNode
            self.tail = newNode
            self.hashMap[key] = newNode
        else:
            newNode = Node(key, value)
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.hashMap[key] = newNode
                
