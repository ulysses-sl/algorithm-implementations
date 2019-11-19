from LinkedList import SinglyLinkedList, DoublyLinkedList


class SLStack:
    def __init__(self):
        self.store = None
        self.count = 0

    def push(self, v):
        x = SinglyLinkedList(v)
        x.next = self.store
        self.count += 1
        self.store = x

    def pop(self):
        if self.store:
            v = self.store.value
            self.store = self.store.next
            self.count -= 1
            return v
        else:
            return None

    def peek(self):
        if self.store:
            return self.store.value
        else:
            return None

    def total(self):
        return self.count


class DLQueue:
    def __init__(self):
        self.head = DoublyLinkedList(None)
        self.tail = DoublyLinkedList(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def push(self, v):
        x = SinglyLinkedList(v)
        # connect x.next
        x.next = self.head.next
        self.head.next.prev = x
        # connect x.prev
        x.prev = self.head
        self.head.next = x
        self.count += 1

    def pop(self):
        if self.count <= 0:
            return None
        v = self.tail.prev.value
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self. tail.prev.prev
        self.count -= 1
        return v

    def peek(self):
        if self.count > 0:
            return self.tail.prev.value
        else:
            return None

    def total(self):
        return self.count


class SQueue:
    def __init__(self):
        self.istack = SLStack()
        self.ostack = SLStack()

    def push(self, v):
        self.istack.push(v)

    def pop(self):
        if self.ostack.count > 0:
            return self.ostack.pop()
        else:
            while self.istack.count > 0:
                self.ostack.push(self.istack.pop())
            if self.ostack.count > 0:
                return self.ostack.pop()
            else:
                return None

    def total(self):
        return self.istack.total() + self.ostack.total()


class QStack1:
    def __init__(self):
        self.q1 = DLQueue()
        self.q2 = DLQueue()

    def push(self, v):
        self.q1.push(v)
        while self.q2.total() > 0:
            self.q1.push(self.q2.pop())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.q2.total() > 0:
            return self.q2.pop()
        else:
            return None

    def total(self):
        return self.q1.total() + self.q2.total()


class QStack2:
    def __init__(self):
        self.q1 = DLQueue()
        self.q2 = DLQueue()

    def push(self, v):
        self.q1.push(v)

    def pop(self):
        if self.q1.count == 0:
            return None
        while self.q1.total() > 1:
            self.q2.push(self.q1.pop())
        v = self.q1.pop()
        self.q1, self.q2 = self.q2, self.q1
        return v

    def total(self):
        return self.q1.total() + self.q2.total()
