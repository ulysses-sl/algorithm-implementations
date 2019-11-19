class HashTableNode:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.next = None


class HashTable:
    def __init__(self, size=100):
        self.table = [None for _ in range(size)]
        self.size = size

    def set(self, k, v):
        i = hash(k) % self.size
        if self.table[i]:
            x = self.table[i]
            while x.next:
                if x.k == k:
                    x.v = v
                    return
            if x.k == k:
                x.v = v
            else:
                x.next = HashTableNode(k, v)
        else:
            self.table[i] = HashTableNode(k, v)

    def get(self, k):
        i = hash(k) % self.size
        x = self.table[i]
        while x:
            if x.k == k:
                return x.v
            x = x.next
        return None
