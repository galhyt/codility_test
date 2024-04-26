import random


class RandomizedSet:

    def __init__(self):
        self.set = []
        self.last_idx = -1

    def search(self, val: int):


    def insert(self, val: int) -> bool:
        idx = self.search(val)
        if idx != -1:
            return False
        self.last_idx += 1
        self.set.append(val)
        return True

    def remove(self, val: int) -> bool:
        idx = self.search(val)
        if idx == -1:
            return False
        self.last_idx -= 1
        self.set.pop(idx)
        return True

    def getRandom(self) -> int:
        idx = random.randint(self.last_idx+1)
        return self.set[idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()