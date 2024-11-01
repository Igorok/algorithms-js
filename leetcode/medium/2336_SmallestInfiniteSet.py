from collections import deque
from typing import List
from json import dumps
import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.set = [i for i in range(1, 1001)]
        heapq.heapify(self.set)

    def popSmallest(self) -> int:
        return heapq.heappop(self.set)

    def addBack(self, num: int) -> None:
        if num not in self.set:
            heapq.heappush(self.set, num)
        return None


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)



def test ():
    params = [
        {
            'input': [
                ["addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"],
                [[2], [], [], [], [1], [], [], []],
            ],
            'output': [None, 1, 2, 3, None, 1, 4, 5],
        },
    ]

    for param in params:
        solution = SmallestInfiniteSet()
        commands, data = param['input']
        for i in range(len(commands)):
            command = commands[i]
            result = None
            if command == 'popSmallest':
                result = solution.popSmallest()
            else:
                result = solution.addBack(data[i][0])

            print(
                'SUCCESS' if result == param['output'][i] else 'ERROR',
                'command', commands[i],
                'output', param['output'][i],
                'result', result,
                '\n',
            )


if __name__ == '__main__':
    test()
