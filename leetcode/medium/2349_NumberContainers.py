class NumberContainers:

    def __init__(self):
        self.numbers = {}
        self.indexes = {}

    def _removeIndex_0(self, index: int):
        n = self.indexes[index]
        i = self.numbers[n].index(index)
        self.numbers[n].pop(i)
        if self.numbers[n]:
            heapq.heapify(self.numbers[n])

    def _removeIndex(self, index: int):
        n = self.indexes[index]
        i = -1
        stack = []
        while i != index:
            i = heapq.heappop(self.numbers[n])
            if i != index:
                stack.append(i)
        for num in stack:
            heapq.heappush(self.numbers[n], num)


    def change(self, index: int, number: int) -> None:
        if index in self.indexes:
            self._removeIndex(index)

        self.indexes[index] = number

        if not number in self.numbers:
            self.numbers[number] = [index]
        else:
            heapq.heappush(self.numbers[number], index)



    def find(self, number: int) -> int:
        if not number in self.numbers or not self.numbers[number]:
            return -1

        return self.numbers[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)




class NumberContainers:

    def __init__(self):
        self.numbers = {}
        self.indexes = {}

    def _removeIndex(self, index: int):
        n = self.indexes[index]
        self.numbers[n].pop(index)

    def change(self, index: int, number: int) -> None:
        if self.indexes[index] == number:
            return

        if index in self.indexes:
            self._removeIndex(index)

        self.indexes[index] = number

        if not number in self.numbers:
            self.numbers[number] = {}
        self.numbers[number][index] = index



    def find(self, number: int) -> int:
        if not number in self.numbers or not self.numbers[number]:
            return -1

        return min(self.numbers[number].values())



class NumberContainers:
    def __init__(self):
        self.numbers = {}
        self.indexes = {}

    def _removeIndex(self, index):
        n = self.indexes[index]

        self.numbers[n]['ids'].pop(index)

        if not self.numbers[n]['ids']:
            self.numbers[n]['min'] = 10e8
            return

        if index == self.numbers[n]['min']:
            self.numbers[n]['min'] = min(self.numbers[n]['ids'].values())

    def change(self, index: int, number: int) -> None:
        if index in self.indexes:
            if self.indexes[index] == number:
                return
            self._removeIndex(index)

        self.indexes[index] = number

        if not number in self.numbers:
            self.numbers[number] = {
                'min': 10e8,
                'ids': {}
            }

        self.numbers[number]['ids'][index] = index
        if index < self.numbers[number]['min']:
            self.numbers[number]['min'] = index


    def find(self, number: int) -> int:
        if not number in self.numbers or not self.numbers[number]['ids']:
            return -1

        return int(self.numbers[number]['min'])


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)