class DequeNode:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev

class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.front = None
        self.last = None

    def insertFront(self, value: int) -> bool:
        if self.size < self.capacity:
            newNode = DequeNode(value, None, self.front)
            if self.size > 0:
                self.front.next = newNode
            self.front = newNode
            if self.size == 0:
                self.last = newNode
            self.size += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.size < self.capacity:
            newNode = DequeNode(value, self.last, None)
            if self.size > 0:
                self.last.prev = newNode
            self.last = newNode
            if self.size == 0:
                self.front = newNode
            self.size += 1
            return True
        else:
            return False


    def deleteFront(self) -> bool:
        if self.size > 0:
            self.front = self.front.prev
            if self.front:
                self.front.next = None
            self.size -= 1
            return True
        else:
            return False
        

    def deleteLast(self) -> bool:
        if self.size > 0:
            self.last = self.last.next
            if self.last:
                self.last.prev = None
            self.size -= 1
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.size > 0:
            return self.front.value
        else:
            return -1

    def getRear(self) -> int:
        if self.size > 0:
            return self.last.value
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

myCircularDeque = MyCircularDeque(3);
myCircularDeque.insertLast(1);
myCircularDeque.insertLast(2);
myCircularDeque.insertFront(3);
myCircularDeque.insertFront(4);
myCircularDeque.getRear();
myCircularDeque.isFull();
myCircularDeque.deleteLast();
myCircularDeque.insertFront(4);
myCircularDeque.getFront();