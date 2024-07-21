#    Main Author(s): Avreet Kaur
#    Main Reviewer(s): Yuvraj Singh & Ravneet Kaur

class HashTable:
    def __init__(self, cap=32):
        self._capacity = cap
        self.size = 0
        self.table = [None] * self._capacity

    def insert(self, key, value):
        index = hash(key) % self._capacity
        if self.table[index] is not None:
            for item in self.table[index]:
                if item[0] == key:
                    return False
            self.table[index].append((key, value))
        else:
            self.table[index] = [(key, value)]
        self.size += 1
        
        if self.size / self._capacity > 0.7:
            self._resize()
        return True

    def modify(self, key, value):
        index = hash(key) % self._capacity
        if self.table[index] is not None:
            for i, item in enumerate(self.table[index]):
                if item[0] == key:
                    self.table[index][i] = (key, value)
                    return True
        return False

    def remove(self, key):
        index = hash(key) % self._capacity
        if self.table[index] is not None:
            for i, item in enumerate(self.table[index]):
                if item[0] == key:
                    self.table[index].pop(i)
                    if len(self.table[index]) == 0:
                        self.table[index] = None
                    self.size -= 1
                    return True
        return False

    def search(self, key):
        index = hash(key) % self._capacity
        if self.table[index] is not None:
            for item in self.table[index]:
                if item[0] == key:
                    return item[1]
        return None

    def capacity(self):
        return self._capacity

    def __len__(self):
        return self.size

    def _resize(self):
        old_table = self.table
        self._capacity *= 2
        self.table = [None] * self._capacity
        self.size = 0

        for chain in old_table:
            if chain is not None:
                for key, value in chain:
                    self.insert(key, value)
