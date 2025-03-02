class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.dict[val] = len(self.list)
            self.list.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.dict:
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx #swap with last element
            self.list.pop()
            del self.dict[val]
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        #set is unorderded, we cannot to indexing so converting to a tuple.
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()