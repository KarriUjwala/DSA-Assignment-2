import random

class RandomizedSet:
    def __init__(self):
        self.v = []
        self.mp = {}

    def search(self, val: int) -> bool:
        return val in self.mp

    def insert(self, val: int) -> bool:
        if self.search(val):
            return False
        self.v.append(val)
        self.mp[val] = len(self.v) - 1
        return True

    def remove(self, val: int) -> bool:
        if not self.search(val):
            return False
        index = self.mp[val]
        last_element = self.v[-1]
        self.v[index] = last_element
        self.mp[last_element] = index
        self.v.pop()
        del self.mp[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.v)



